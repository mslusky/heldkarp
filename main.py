# This is a sample file for running the heldkarp algorithm

import heldkarp
import test_graphs

heldkarp.find_lower_bound(test_graphs.g1)
heldkarp.find_lower_bound(test_graphs.g2)
heldkarp.find_lower_bound(test_graphs.bayg29())

# random graph on 30 vertices. Each edge has p=.5 of being 
# present in the graph. The weights are integers 1 to 10. The 
# seed is 123456
random_graph = test_graphs.get_random_connected_graph(30, .5, 10, 123456)

heldkarp.find_lower_bound(random_graph)



