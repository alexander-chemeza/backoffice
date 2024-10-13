from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create user roles and assign permissions'

    def handle(self, *args, **kwargs):
        # Define roles
        roles = ['administrator', 'manager', 'operator', 'marketer']

        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Group "{role}" created.'))
            else:
                self.stdout.write(f'Group "{role}" already exists.')

        # Assign permissions (example)
        admin_group = Group.objects.get(name='administrator')
        admin_permissions = Permission.objects.filter(codename__in=[
            'add_advertisements',
            'add_contracts',
            'add_customer',
            'add_profile',
            'add_services',
            'add_user',
            'change_advertisements',
            'change_contracts',
            'change_customer',
            'change_profile',
            'change_services',
            'change_user',
            'delete_advertisements',
            'delete_contracts',
            'delete_customer',
            'delete_profile',
            'delete_services',
            'delete_user',
            'view_advertisements',
            'view_contracts',
            'view_customer',
            'view_group',
            'view_profile',
            'view_services',
            'view_user',
        ])
        admin_group.permissions.set(admin_permissions)
        # admin_group.permissions.set(Permission.objects.all())  # All permissions

        # Restrict administrator group from creating other administrators
        # create_admin_perm = Permission.objects.get(codename='add_user')
        # admin_group.permissions.remove(create_admin_perm)

        # Assign specific permissions to other groups
        manager_group = Group.objects.get(name='manager')
        operator_group = Group.objects.get(name='operator')
        marketer_group = Group.objects.get(name='marketer')

        # Example: Allow managers to view and edit leads
        manager_permissions = Permission.objects.filter(codename__in=[
            'view_customer',
            'view_contracts',
            'add_customer',
            'add_contracts',
            'change_customer',
            'change_contracts',
            'delete_customer',
            'delete_contracts'
        ])
        manager_group.permissions.set(manager_permissions)

        # Example: Allow operators to view contracts
        operator_permissions = Permission.objects.filter(codename__in=[
            'view_customer',
            'add_customer',
            'change_customer',
            'delete_customer'
        ])
        operator_group.permissions.set(operator_permissions)

        marketer_permissions = Permission.objects.filter(codename__in=[
            'view_services',
            'view_advertisements',
            'add_services',
            'add_advertisements',
            'change_services',
            'change_advertisements',
            'delete_services',
            'delete_advertisements'
        ])

        marketer_group.permissions.set(marketer_permissions)

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been assigned.'))
