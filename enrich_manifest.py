import json

with open('original-manifest.json') as json_file:
    original_mainfest_data = json.load(json_file)

for canvas in original_mainfest_data['items']:
    id = canvas['id']
    # extract the numeric id from the uri (https://lbiiif.riksarkivet.se/arkis!30003111_00004/canvas -> 30003111_00004)
    id = id.split('/')[-2].split('!')[-1]

    canvas['seeAlso'] = {
        '@id': f'https://byabbe.se/riksarkivet-text/alto/{id}.xml',
        'profile': 'http://www.loc.gov/standards/alto/ns-v4#',
        'format': 'application/xml'
    }

# write to new file
with open('enriched_manifest.json', 'w') as outfile:
    json.dump(original_mainfest_data, outfile, indent=4)
