from app1.models import UserProfile

# Get all user profiles
user_profiles = UserProfile.objects.all()
for user in user_profiles:
    print(user.fullname, user.email, user.phone, user.address, user.password)
