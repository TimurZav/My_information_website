from django.db import models
from django.utils.safestring import mark_safe
import json


class PrettyJSONEncoder(json.JSONEncoder):
    def __init__(self, *args, indent, ensure_ascii, sort_keys, **kwargs):
        super().__init__(*args, indent=2, ensure_ascii=False, sort_keys=True, **kwargs)


class Import(models.Model):
    import_id = models.IntegerField(primary_key=True)
    ship = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    terminal = models.CharField(max_length=20, blank=True, null=True)
    container_number = models.CharField(max_length=20, blank=True, null=True)
    container_size = models.IntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=10, blank=True, null=True)
    goods_name_rus = models.CharField(max_length=1500, blank=True, null=True)
    consignment = models.CharField(max_length=100, blank=True, null=True)
    shipper = models.CharField(max_length=500, blank=True, null=True)
    consignee = models.CharField(max_length=500, blank=True, null=True)
    line = models.CharField(max_length=500, blank=True, null=True)
    count = models.CharField(max_length=1500, blank=True, null=True)
    teu = models.IntegerField(blank=True, null=True)
    voyage = models.CharField(max_length=1500, blank=True, null=True)
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

    def _do_insert(self, manager, using, fields, update_pk, raw):
        fields = [
            f for f in fields if f.attname not in ['teu', 'year', 'month', 'month_parsed_on', 'year_parsed_on']
        ]
        return super()._do_insert(manager, using, fields, update_pk, raw)

    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        values = [
            value for value in values if value[0].attname not in ['teu', 'year', 'month', 'month_parsed_on', 'year_parsed_on']
        ]
        return super()._do_update(base_qs, using, pk_val, values, update_fields, forced_update)

    class Meta:
        managed = False
        db_table = 'import'


class Port(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(null=True, upload_to='upload/', blank=True)
    url_image = models.CharField(max_length=500)
    data_json = models.JSONField(max_length=50000, blank=True, null=True, encoder=PrettyJSONEncoder)
    
    def __str__(self):
        return self.url_image


    @property
    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="826" height="1169" />')
        return ""
    
    @property
    def label_from_json(self):
        if self.data_json:
            return self.data_json[0]["text"][0]["text"]
        return ""
    
    @property
    def date_from_json(self):
        if self.data_json:
            return self.data_json[0]["text"][1]["text"]
        return ""
    
    @property
    def table_from_json(self):
        if self.data_json:
            for data in self.data_json:
                for text in data:
                    try:
                        print(text["cells"])
                    except:
                        pass
            # return json.dumps(self.data_json[0][0], ensure_ascii=False)
        return ""

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'port'


class ExamplePosts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_posts'


class Line(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(null=True, upload_to='upload/', blank=True)
    url_image = models.CharField(max_length=500)
    data_json = models.JSONField(max_length=50000, blank=True, null=True, encoder=PrettyJSONEncoder)

    class Meta:
        managed = False
        db_table = 'line'


