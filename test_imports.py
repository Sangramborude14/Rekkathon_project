#!/usr/bin/env python
"""Test if all imports work correctly"""

print("Testing imports...")

try:
    from config.settings import settings
    print("✓ Settings imported successfully")
    print(f"  - MONGODB_URL: {settings.MONGODB_URL}")
    print(f"  - DATABASE_NAME: {settings.DATABASE_NAME}")
except Exception as e:
    print(f"✗ Settings import failed: {e}")
    exit(1)

try:
    from backend.models.database import connect_to_mongo
    print("✓ Database module imported successfully")
except Exception as e:
    print(f"✗ Database import failed: {e}")
    exit(1)

try:
    from backend.main import app
    print("✓ FastAPI app imported successfully")
except Exception as e:
    print(f"✗ FastAPI app import failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n✓ All imports successful!")
