import json
import requests
import os
from datetime import datetime
from typing import Dict, Optional, Tuple

class LicenseManager:
    """
    Manages license verification for Open EProS system.
    Supports both individual user licenses and department-based access.
    """

    def __init__(self):
        self.license_url = "https://raw.githubusercontent.com/SamMachariaPhD/exam-system-auth/main/licenses.json"
        self.cache_file = "auth_cache.json"
        self.cache_duration = 86400  # 24 hours in seconds

    def verify_license(self, email: str) -> Tuple[bool, str, Dict]:
        """
        Verify if an email has valid license access.

        Args:
            email (str): User's email address

        Returns:
            Tuple[bool, str, Dict]: (is_valid, message, license_data)
        """
        try:
            # Try to get license data from online source
            license_data = self._fetch_license_data()

            if not license_data:
                # Fallback to cache if available
                license_data = self._load_cache()
                if not license_data:
                    return False, "Unable to verify license. No internet connection and no cached data.", {}

            # Check individual user license
            user_license = self._check_user_license(email, license_data)
            if user_license[0]:
                return user_license

            # Check department access
            dept_license = self._check_department_access(email, license_data)
            if dept_license[0]:
                return dept_license

            return False, f"Email {email} is not authorized to use this system.", {}

        except Exception as e:
            return False, f"License verification failed: {str(e)}", {}

    def _fetch_license_data(self) -> Optional[Dict]:
        """Fetch license data from online source."""
        try:
            response = requests.get(self.license_url, timeout=10)
            response.raise_for_status()

            license_data = response.json()

            # Cache the data for offline use
            self._save_cache(license_data)

            return license_data
        except Exception:
            return None

    def _check_user_license(self, email: str, license_data: Dict) -> Tuple[bool, str, Dict]:
        """Check if user has individual license."""
        user_licenses = license_data.get("licenses", {})

        if email in user_licenses:
            user_data = user_licenses[email]

            # Check if license is active
            if not user_data.get("active", False):
                return False, f"License for {email} is inactive.", {}

            # Check expiration date
            expires = user_data.get("expires", "")
            if expires and datetime.now() > datetime.strptime(expires, "%Y-%m-%d"):
                return False, f"License for {email} has expired.", {}

            return True, f"Welcome {email}! Individual license verified.", user_data

        return False, "", {}

    def _check_department_access(self, email: str, license_data: Dict) -> Tuple[bool, str, Dict]:
        """Check if user has department-based access."""
        dept_access = license_data.get("department_access", {})

        for dept_key, dept_data in dept_access.items():
            if not dept_data.get("active", False):
                continue

            # Check email domain matches
            email_domains = dept_data.get("email_domains", [])
            user_domain = "@" + email.split("@")[-1] if "@" in email else ""

            if user_domain in email_domains:
                # Check expiration
                expires = dept_data.get("expires", "")
                if expires and datetime.now() > datetime.strptime(expires, "%Y-%m-%d"):
                    continue

                dept_name = dept_data.get("department", "Department")
                institution = dept_data.get("institution", "Institution")

                return True, f"Welcome! Access granted via {dept_name}, {institution}", dept_data

        return False, "", {}

    def _save_cache(self, data: Dict):
        """Save license data to local cache."""
        try:
            cache_data = {
                "timestamp": datetime.now().isoformat(),
                "data": data
            }
            with open(self.cache_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
        except Exception:
            pass  # Ignore cache save errors

    def _load_cache(self) -> Optional[Dict]:
        """Load license data from local cache if recent."""
        try:
            if not os.path.exists(self.cache_file):
                return None

            with open(self.cache_file, 'r') as f:
                cache_data = json.load(f)

            # Check if cache is still valid
            cache_time = datetime.fromisoformat(cache_data["timestamp"])
            if (datetime.now() - cache_time).total_seconds() > self.cache_duration:
                return None

            return cache_data["data"]
        except Exception:
            return None

    def get_system_message(self) -> str:
        """Get system message from license data."""
        try:
            license_data = self._fetch_license_data() or self._load_cache()
            if license_data:
                return license_data.get("system_message", "Welcome to Open EProS!")
        except Exception:
            pass
        return "Welcome to Open EProS!"

    def check_update_required(self) -> Tuple[bool, str]:
        """Check if system update is required."""
        try:
            license_data = self._fetch_license_data() or self._load_cache()
            if license_data:
                update_required = license_data.get("update_required", False)
                download_url = license_data.get("download_url", "")
                return update_required, download_url
        except Exception:
            pass
        return False, ""