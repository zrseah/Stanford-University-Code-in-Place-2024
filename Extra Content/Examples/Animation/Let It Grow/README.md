# Instruction 
Sometimes when animating, we want to give the appearance that something is changing shape. This may mean that an object is getting smaller/larger, stretched, or transformed in some other way. 

Our canvas doesn't have a direct way to perform these transformations, but it is still possible with a little workaround! This can be done by:

Storing the information about a shape from our canvas

Deleting the original shape from the canvas

Using the stored information to remake the object with any transformations we may like.

To practice this, fill out the grow_leaves(...) function. We can grow our leaves by making new leaves which are just slightly larger circles than before. If we do this many times, it will look like the leaves are growing! Make sure to grow the leaves by a factor of GROWTH_FACTOR.

(Hint: You may find the get_corner_coordinates(...) function handy! It stores a shape's top left and bottom right points in the form of (left_x, top_y, right_x, bottom_y).)

## Let It Grow
![Let It Grow](https://github.com/user-attachments/assets/b60aff7f-59f5-4886-a387-1ee7f9002191)

Click [here](https://codeinplace.stanford.edu/cip4/share/8kMRQsUCZUhcyoyN4ZQA) to view animation.
