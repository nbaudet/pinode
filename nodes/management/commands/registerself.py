from django.core.management.base import BaseCommand, CommandError
from nodes.management.commands._utils import CommandUtils
from nodes.models import Node


class Command(BaseCommand):
    help = 'Register or update the current node with its name in the database\
        and mark it as self=True'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        utils = CommandUtils(self)
        name = options['name'][0]
        node = None

        # Try to get existing Node with self=True
        try:
            node = Node.objects.get(is_self=True)
        except Node.DoesNotExist:
            pass

        # Verify there is not another Node with same name which is not self
        try:
            node_with_same_name = Node.objects.get(name=name)
            if not(node_with_same_name.is_self):
                raise CommandError('This name is already in use by another Node')
        except Node.DoesNotExist:
            pass

        # Create or update Node
        if node is None:
            Node.objects.create(name=name, is_self=True, ip_address=utils.get_ip(),
                mac_address=utils.get_mac())
            created = True
        else:
            node.name = name
            node.ip_address = utils.get_ip()
            node.mac_address = utils.get_mac()
            node.save()
            created = False

        if created:
            utils.success(f'Node {name} was created successfully')
        else:
            utils.success(f'Node {name} was updated')
