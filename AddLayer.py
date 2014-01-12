# I plan to add some technical things later to improve performance, please
# ignore code that is commented out.

inputs = (
  ("Surface block type:", "blocktype"),
  ("Cover:", ("Only this type", "All but this type")),
  ("Ignore block data?", False),
  ("Cover block type:", "blocktype"),
  #("Access method", ("Use blockAt", "Use temp schematic", "Use chunk slices")),
)

def perform(level, box, options):
    surfaceType     = options["Surface block type:"].ID
    surfaceTypeData = options["Surface block type:"].blockData
    coverType     = options["Cover block type:"].ID
    coverTypeData = options["Cover block type:"].blockData
    ignoreData = options["Ignore block data?"]
    coverPolicy = (options["Cover:"] == "Only this type")
    #method = options["Access method"]

    if True: #method == "Use blockAt":
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.maxy, box.miny-1, -1):
                    if level.blockAt(x, y, z) != 0:
                        if (level.blockAt(x, y, z) == surfaceType and (level.blockDataAt(x, y, z) == surfaceTypeData or ignoreData)) == coverPolicy:
                            level.setBlockAt(x, y+1, z, coverType)
                            level.setBlockDataAt(x, y+1, z, coverTypeData)
                        break
'''
    elif method == "Use temp schematic":
        raise NotImplementedError("Temp schematic method not yet implemented!")
        temp = level.extractSchematic(box)

        # remove any entities in the temp.  this is an ugly move
        # because copyBlocksFrom actually copies blocks, entities, everything
        temp.removeEntitiesInBox(temp.bounds)
        temp.removeTileEntitiesInBox(temp.bounds)

        # replaces gold with TNT.
        # the expression in [] creates a temporary the same size, using more memory
        temp.Blocks[temp.Blocks == 14] = 46

        level.copyBlocksFrom(temp, temp.bounds, box.origin)

    elif method == "Use chunk slices":
        raise NotImplementedError("Chunk slice method not yet implemented!")
        for (chunk, slices, point) in level.getChunkSlices(box):
            # chunk is an AnvilChunk object with attributes:
            # Blocks, Data, Entities, and TileEntities
            # Blocks and Data can be indexed using slices:
            blocks = chunk.Blocks[slices]

            # blocks now contains a "view" on the part of the chunk's blocks
            # that lie in the selection. This "view" is a numpy object that
            # accesses only a subsection of the original array, without copying

            # once again, gold into TNT
            blocks[blocks == 14] = 46

            # notify the world that the chunk changed
            # this gives finer control over which chunks are dirtied
            # you can call chunk.chunkChanged(False) if you want to dirty it
            # but not run the lighting calc later.

            chunk.chunkChanged()
    else:
        raise NotImplementedError("That access method is not implemented!")
'''
