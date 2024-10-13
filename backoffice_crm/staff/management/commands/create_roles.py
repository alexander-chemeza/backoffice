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
            'add_ads',
            'add_contracts',
            'add_leads',
            'add_customers',
            'add_staff',
            'add_products',
            'add_user',
            'change_ads',
            'change_contracts',
            'change_leads',
            'change_customers',
            'change_staff',
            'change_products',
            'change_user',
            'delete_ads',
            'delete_contracts',
            'delete_leads',
            'delete_customers',
            'delete_staff',
            'delete_products',
            'delete_user',
            'view_ads',
            'view_contracts',
            'view_leads',
            'view_customers',
            'view_group',
            'view_staff',
            'view_products',
            'view_user',
        ])
        admin_group.permissions.set(admin_permissions)

        manager_group = Group.objects.get(name='manager')
        operator_group = Group.objects.get(name='operator')
        marketer_group = Group.objects.get(name='marketer')

        manager_permissions = Permission.objects.filter(codename__in=[
            'view_customers',
            'view_contracts',
            'add_customers',
            'add_contracts',
            'change_customers',
            'change_contracts',
            'delete_customers',
            'delete_contracts'
        ])
        manager_group.permissions.set(manager_permissions)

        # Example: Allow operators to view contracts
        operator_permissions = Permission.objects.filter(codename__in=[
            'view_customers',
            'add_customers',
            'change_customers',
            'delete_customers',
            'view_leads',
            'add_leads',
            'change_leads',
            'delete_leads',
        ])
        operator_group.permissions.set(operator_permissions)

        marketer_permissions = Permission.objects.filter(codename__in=[
            'view_products',
            'view_ads',
            'add_products',
            'add_ads',
            'change_products',
            'change_ads',
            'delete_products',
            'delete_ads'
        ])

        marketer_group.permissions.set(marketer_permissions)

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been assigned.'))
