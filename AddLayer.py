inputs = (
       ("Surface block type:", "blocktype"),
       ("Cover:", ("Only this type", "All but this type")),
       ("Ignore block data?", False),
       ("Cover block type:", "blocktype"))

def perform(level, box, options):
    surfaceType     = options["Surface block type:"].ID
    surfaceTypeData = options["Surface block type:"].blockData
    coverType     = options["Cover block type:"].ID
    coverTypeData = options["Cover block type:"].blockData
    ignoreData = options["Ignore block data?"]
    coverPolicy = (options["Cover:"] == "Only this type")

    for x in xrange(box.minx, box.maxx):
        for z in xrange(box.minz, box.maxz):
            for y in xrange(box.maxy, box.miny-1, -1):
                if level.blockAt(x, y, z) != 0:
                    if (level.blockAt(x, y, z) == surfaceType and (level.blockDataAt(x, y, z) == surfaceTypeData or ignoreData)) == coverPolicy:
                        level.setBlockAt(x, y+1, z, coverType)
                        level.setBlockDataAt(x, y+1, z, coverTypeData)
                    break

