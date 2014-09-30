inputs = (
       ("Surface block type:", "blocktype"),
       ("Cover:"             , ("Only this type", "All but this type")),
       ("Ignore block data?" , False),
       ("Cover block type:"  , "blocktype"))

def perform(level, box, options):
    surfaceType = options["Surface block type:"].ID
    surfaceData = options["Surface block type:"].blockData
    coverType   = options["Cover block type:"  ].ID
    coverData   = options["Cover block type:"  ].blockData
    ignoreData  = options["Ignore block data?" ]
    coverPolicy = options["Cover:"             ] == "Only this type"
    
    for x in xrange(box.minx, box.maxx):
        for z in xrange(box.minz, box.maxz):
            for y in xrange(box.maxy, box.miny-1, -1):
                blockType = level.blockAt(x, y, z)
                blockData = level.blockDataAt(x, y, z)
                if blockType != 0:
                    if (blockType==surfaceType and (blockData==surfaceData or ignoreData)) == coverPolicy:
                        level.setBlockAt(x, y+1, z, coverType)
                        level.setBlockDataAt(x, y+1, z, coverData)
                    break

