from django.urls import path
from .views import hello, list_school_admins, create_admin, getPlatformAdmins, getAdminById, getPlatformGroups, getGroupById, createAccessExternal, loginAccess
# relevant patterns


urlpatterns = [
    path('greetings/', hello, name='Hello'),
    path('school-create/', create_admin, name='Create School Admin'),
    path('school-admins/', list_school_admins, name='List School Admins'),
    # platform admins
    path('platform-admins/', getPlatformAdmins, name='List platform admins'),
    path('platform-admins/<int:admin_id>/', getAdminById, name='List admin by id'),
    path('platform-groups/', getPlatformGroups, name='Platforms Groups'),
    path('platform-groups/<int:group_id>/', getGroupById, name='Group by id'),
    # external access
    path('external-access/', createAccessExternal, name='Create external access'),
    path('external-login-access/', loginAccess, name='Login to access dashboard')
]