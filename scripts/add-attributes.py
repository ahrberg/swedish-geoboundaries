### simple script to add regions and municipality
### attributes and fields to layer
### modify path to csv and shape file to run
### purpose built, will only work for this special case

import csv

# regions etc in csv file
csv_path = "../data/regions.csv"
# shape file to add attributes to
path = "../data/boundaries.shp"

with open(csv_path, newline='') as csvfile:
    csv_data = list(csv.DictReader(csvfile, delimiter=';'))

    layer = QgsVectorLayer(path, "", "ogr")
    
    pr = layer.dataProvider()
    # add fields
    pr.addAttributes([QgsField("LANDS_NR", QVariant.Int),
                        QgsField("LANDSD", QVariant.String),
                        QgsField("LANSK_NR", QVariant.Int),
                        QgsField("LANDSK", QVariant.String),
                        QgsField("LÄN_NR", QVariant.Int),
                        QgsField("LÄN", QVariant.String),
                        QgsField("KOMMUN_NR", QVariant.Int),
                        QgsField("KOMMUN", QVariant.String)])
    layer.updateFields() # tell the vector layer to fetch changes from the provider

    fc = layer.featureCount()
    
    it = layer.getFeatures()
    
    layer.startEditing()
    
    for feat in it:
        code = feat["DISTRKOD"]
        found = 0
        for row in csv_data:
            if(str(code) == row["LLD-kod"]):
                layer.changeAttributeValue(feat.id(), 5,int(row["Landsdels-nr"]))
                layer.changeAttributeValue(feat.id(), 6,row["Landsdel"])
                layer.changeAttributeValue(feat.id(), 7,int(row["Landskaps-nr"]))
                layer.changeAttributeValue(feat.id(), 8,row["Landskap"])
                layer.changeAttributeValue(feat.id(), 9,int(row["Län-nr"]))
                layer.changeAttributeValue(feat.id(), 10,row["Län"])
                layer.changeAttributeValue(feat.id(), 11,int(row["Kommun-nr"]))
                layer.changeAttributeValue(feat.id(), 12,row["Kommun"])
                found = 1
                break
        if (found == 0):
            print("Not found", code)
    layer.commitChanges()

print("DONE")
            