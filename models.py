# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True, max_length=-1)
    value = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmptyContainerSample(models.Model):
    sample = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'empty_container_sample'


class Export(models.Model):
    goods_tnved = models.CharField(max_length=20, blank=True, null=True)
    goods_name = models.CharField(max_length=500, blank=True, null=True)
    container_number = models.CharField(max_length=20, blank=True, null=True)
    ship_name = models.CharField(max_length=100, blank=True, null=True)
    ship_owner = models.CharField(max_length=20, blank=True, null=True)
    ship_imo = models.CharField(max_length=20, blank=True, null=True)
    expeditor = models.CharField(max_length=500, blank=True, null=True)
    shiper = models.CharField(max_length=500, blank=True, null=True)
    consignee = models.CharField(max_length=500, blank=True, null=True)
    shipper_terminal = models.CharField(max_length=20, blank=True, null=True)
    shipper_seaport = models.CharField(max_length=20, blank=True, null=True)
    consignee_seaport = models.CharField(max_length=20, blank=True, null=True)
    order_number = models.CharField(max_length=20, blank=True, null=True)
    original_file_name = models.CharField(max_length=200, blank=True, null=True)
    order_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export'


class ExportFinalDestination(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    last_date_of_month = models.TextField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    seaport = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    ship_name = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_final_destination'


class ExportView(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    goods_tnved = models.TextField(blank=True, null=True)
    goods_name = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    ship_name_er = models.TextField(db_column='ship_name.er', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ship_owner = models.TextField(blank=True, null=True)
    ship_imo = models.TextField(blank=True, null=True)
    expeditor = models.TextField(blank=True, null=True)
    shiper = models.TextField(blank=True, null=True)
    consignee = models.TextField(blank=True, null=True)
    shipper_terminal = models.TextField(blank=True, null=True)
    shipper_seaport = models.TextField(blank=True, null=True)
    consignee_seaport = models.TextField(blank=True, null=True)
    order_number = models.TextField(blank=True, null=True)
    original_file_name = models.TextField(blank=True, null=True)
    order_date = models.TextField(blank=True, null=True)
    order_month = models.FloatField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_size = models.TextField(blank=True, null=True)
    index = models.FloatField(blank=True, null=True)
    last_date_of_month = models.TextField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    final_destination_seaport = models.TextField(blank=True, null=True)
    final_destination_country = models.TextField(blank=True, null=True)
    ship_name = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    order_month_track = models.FloatField(db_column='order_month.track', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'export_view'


class ExportViewCoords(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    goods_tnved = models.BigIntegerField(blank=True, null=True)
    goods_name = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    ship_name_er = models.TextField(db_column='ship_name.er', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ship_owner = models.TextField(blank=True, null=True)
    ship_imo = models.TextField(blank=True, null=True)
    expeditor = models.TextField(blank=True, null=True)
    shiper = models.TextField(blank=True, null=True)
    consignee = models.TextField(blank=True, null=True)
    shipper_terminal = models.TextField(blank=True, null=True)
    shipper_seaport = models.TextField(blank=True, null=True)
    consignee_seaport = models.TextField(blank=True, null=True)
    order_number = models.TextField(blank=True, null=True)
    original_file_name = models.TextField(blank=True, null=True)
    order_date = models.TextField(blank=True, null=True)
    order_month = models.FloatField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_size = models.FloatField(blank=True, null=True)
    index = models.FloatField(blank=True, null=True)
    last_date_of_month = models.TextField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    final_destination_seaport = models.TextField(blank=True, null=True)
    final_destination_country = models.TextField(blank=True, null=True)
    ship_name = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    order_month_track = models.FloatField(db_column='order_month.track', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    teu = models.BigIntegerField(blank=True, null=True)
    is_direction = models.TextField(blank=True, null=True)
    lat_port = models.FloatField(blank=True, null=True)
    long_port = models.FloatField(blank=True, null=True)
    lat_city = models.FloatField(blank=True, null=True)
    long_city = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_view_coords'


class FullImportExport(models.Model):
    is_direction = models.TextField(blank=True, null=True)
    teu = models.BigIntegerField(blank=True, null=True)
    lat_port = models.FloatField(blank=True, null=True)
    long_port = models.FloatField(blank=True, null=True)
    lat_city = models.FloatField(blank=True, null=True)
    long_city = models.FloatField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    shipper_country = models.TextField(blank=True, null=True)
    shipper_seaport = models.TextField(blank=True, null=True)
    ship = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_size = models.FloatField(blank=True, null=True)
    shipper = models.TextField(blank=True, null=True)
    goods_name_rus = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'full_import_export'


class FullImportFinal(models.Model):
    import_id = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    container_size = models.BigIntegerField(blank=True, null=True)
    teu = models.BigIntegerField(blank=True, null=True)
    goods_name_rus = models.TextField(blank=True, null=True)
    ship = models.TextField(blank=True, null=True)
    shipper = models.TextField(blank=True, null=True)
    consignee = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    consignment = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    goods_tnved = models.FloatField(blank=True, null=True)
    shipper_seaport = models.TextField(blank=True, null=True)
    shipper_country = models.TextField(blank=True, null=True)
    is_direction = models.TextField(blank=True, null=True)
    lat_port = models.FloatField(blank=True, null=True)
    long_port = models.FloatField(blank=True, null=True)
    lat_city = models.FloatField(blank=True, null=True)
    long_city = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'full_import_final'


class Import(models.Model):
    ship = models.CharField(max_length=100, blank=True, null=True)
    import_id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    terminal = models.CharField(max_length=20, blank=True, null=True)
    container_number = models.CharField(max_length=20, blank=True, null=True)
    container_size = models.IntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=10, blank=True, null=True)
    goods_name_rus = models.CharField(max_length=1500, blank=True, null=True)
    consignment = models.CharField(max_length=100, blank=True, null=True)
    shipper = models.CharField(max_length=500, blank=True, null=True)
    consignee = models.CharField(max_length=500, blank=True, null=True)
    line = models.CharField(max_length=-1, blank=True, null=True)
    count = models.CharField(max_length=-1, blank=True, null=True)
    teu = models.IntegerField(blank=True, null=True)
    voyage = models.CharField(max_length=-1, blank=True, null=True)
    shipper_country = models.CharField(max_length=50, blank=True, null=True)
    goods_weight = models.FloatField(blank=True, null=True)
    package_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    shipper_seaport = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    goods_tnved = models.CharField(max_length=20, blank=True, null=True)
    parsed_on = models.DateField(blank=True, null=True)
    month_parsed_on = models.IntegerField(blank=True, null=True)
    year_parsed_on = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import'


class ImportFinalDestination(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    seaport = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    ship = models.TextField(blank=True, null=True)
    consignment = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_final_destination'


class ImportFinalLonLat(models.Model):
    import_id = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    container_size = models.BigIntegerField(blank=True, null=True)
    teu = models.BigIntegerField(blank=True, null=True)
    goods_name_rus = models.TextField(blank=True, null=True)
    ship = models.TextField(blank=True, null=True)
    shipper = models.TextField(blank=True, null=True)
    consignee = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    consignment = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    goods_tnved = models.FloatField(blank=True, null=True)
    shipper_seaport = models.TextField(blank=True, null=True)
    shipper_country = models.TextField(blank=True, null=True)
    lat_port = models.FloatField(blank=True, null=True)
    long_port = models.FloatField(blank=True, null=True)
    lat_city = models.FloatField(blank=True, null=True)
    long_city = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_final_lon_lat'


class ImportFinalWithCoord(models.Model):
    import_id = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    container_size = models.BigIntegerField(blank=True, null=True)
    teu = models.BigIntegerField(blank=True, null=True)
    goods_name_rus = models.TextField(blank=True, null=True)
    ship = models.TextField(blank=True, null=True)
    shipper = models.TextField(blank=True, null=True)
    consignee = models.TextField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    consignment = models.TextField(blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    goods_tnved = models.FloatField(blank=True, null=True)
    shipper_seaport = models.TextField(blank=True, null=True)
    shipper_country = models.TextField(blank=True, null=True)
    is_direction = models.TextField(blank=True, null=True)
    lat_port = models.FloatField(blank=True, null=True)
    long_port = models.FloatField(blank=True, null=True)
    lat_city = models.FloatField(blank=True, null=True)
    long_city = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_final_with_coord'


class ReferenceContainerType(models.Model):
    container_type = models.CharField(primary_key=True, max_length=-1)
    container_type_unified = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_container_type'


class ReferenceLines(models.Model):
    line = models.CharField(primary_key=True, max_length=-1)
    line_unified = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_lines'


class ReferenceMorservice(models.Model):
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    direction = models.CharField(max_length=-1, blank=True, null=True)
    is_empty = models.BooleanField(blank=True, null=True)
    container_type = models.CharField(max_length=-1, blank=True, null=True)
    teu = models.FloatField(blank=True, null=True)
    is_ref = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_morservice'


class ReferenceRegion(models.Model):
    seaport = models.CharField(max_length=-1, blank=True, null=True)
    seaport_unified = models.CharField(max_length=-1, blank=True, null=True)
    country = models.CharField(max_length=-1, blank=True, null=True)
    region = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_region'


class ReferenceShip(models.Model):
    ship_name = models.CharField(max_length=-1, blank=True, null=True)
    ship_name_unified = models.CharField(max_length=-1, blank=True, null=True)
    ship_imo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_ship'


class ReportOnOrders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    date_departure = models.TextField(blank=True, null=True)
    order_number = models.TextField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    expeditor = models.TextField(blank=True, null=True)
    goods_name = models.TextField(blank=True, null=True)
    date_arrived = models.TextField(blank=True, null=True)
    date_shipped = models.TextField(blank=True, null=True)
    destination_seaport = models.TextField(blank=True, null=True)
    ship_name = models.TextField(blank=True, null=True)
    container_type = models.TextField(blank=True, null=True)
    container_size = models.TextField(blank=True, null=True)
    container_number = models.TextField(blank=True, null=True)
    order_year = models.BigIntegerField(blank=True, null=True)
    order_month = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_on_orders'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Statistics(models.Model):
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    ship_name = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=10, blank=True, null=True)
    is_empty = models.BooleanField(blank=True, null=True)
    line = models.CharField(max_length=20, blank=True, null=True)
    container_size = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    teu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics'


class TerminalMap(models.Model):
    terminal_map_id = models.IntegerField(primary_key=True)
    rus = models.CharField(max_length=-1, blank=True, null=True)
    eng = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terminal_map'
