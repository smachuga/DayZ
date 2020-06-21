import xml.etree.ElementTree as ET

def search():
    from xml.dom import minidom
    mydoc = minidom.parse('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    items = mydoc.getElementsByTagName('tag')
    return [item.attributes['name'].value for item in sorted(items, key=lambda x: x.attributes['name'].value)]

def post(value):
    if value.lower() in search():
        return 'Server Error', 500, {'x-error': 'tag already exists'}

    import xml.etree.ElementTree as ET
    tree = ET.parse('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    root = tree.getroot()
    container = root.find('tags')
    element = container.makeelement('tag', {'name':value.lower()})
    container.append(element)
    tree.write('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    return 'Success', 200

def delete(value):
    # TODO: Remove all usages of tag in other files

    if not value.lower() in search():
        return 'Not Found', 404, {'x-error': 'tag does not exist'}

    tree = ET.parse('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    root = tree.getroot()
    container = root.find('tags')
    for elem in container.findall(f'.//tag[@name="{value.lower()}"]'):
        container.remove(elem)         
    tree.write('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    return 'Success', 200