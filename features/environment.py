def before_all(context):
    context.saved_data = {}

def after_all(context):
    context.saved_data.clear()