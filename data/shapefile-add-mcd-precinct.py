from dbfpy import dbf

in_dbf = dbf.Dbf("../shapefiles/vtd_20101029.dbf")
out_dbf = dbf.Dbf("../shapefiles/out/vtd_20101029.dbf", new=True)

for fieldDef in in_dbf.fieldDefs:
    out_dbf.addField(fieldDef)

out_dbf.addField( ("CTUPRE", "C", 15), )

for in_rec in in_dbf:
    out_rec = out_dbf.newRecord()
    for fieldName in in_dbf.fieldNames:
        out_rec[fieldName] = in_rec[fieldName]
    out_rec["CTUPRE"] = str(int(in_rec["CTU_CODE"])) + ":" + str(int(in_rec["PRECINCT_N"]))
    out_rec.store()

in_dbf.close()
out_dbf.close()

