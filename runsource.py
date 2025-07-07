import pandas as pd
from aizynthfinder.reactiontree import ReactionTree
data = pd.read_json("output.json.gz", orient="table")
all_trees = data.trees.values
for index, trees_for_first_target in enumerate(all_trees):
    for itree, tree in enumerate(trees_for_first_target):
        imagefile = "routes/"+str(index+1)+"_"+f"route{itree:03d}.png"
        ReactionTree.from_dict(tree).to_image(show_all=True).save(imagefile)
        print([i.inchi for i in list(ReactionTree.from_dict(tree).leafs())])
