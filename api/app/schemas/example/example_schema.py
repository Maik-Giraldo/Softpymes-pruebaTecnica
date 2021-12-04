from app import ma

class ExampleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name',  'identification', 'description', 'status', 'create_date', 'update_date')

example = ExampleSchema()

examples = ExampleSchema(many=True)