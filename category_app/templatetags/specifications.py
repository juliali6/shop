from django import template
from django.utils.safestring import mark_safe

register = template.Library()


TABLE_HEAD = """
                <table class="table">
                    <tbody>
            """

TABLE_TAIL = """
                </tbody>
                    </table>

            """

TABLE_CONTENT = """
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Processor freq': 'processor_freq',
        'Ram': 'ram',
        'Video card': 'video',
        'Battery life': 'time_without_charge',
    },
    'smartphone': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Screen resolution': 'resolution',
        'Battery capacity': 'accum_volume',
        'Ram': 'ram',
        'Sd card': 'sd',
        'Maximum built-in memory': 'sd_volume_max',
        'Main camera': 'main_cam_mp',
        'Front camera': 'frontal_cam_mp',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
