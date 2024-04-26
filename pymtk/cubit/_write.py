# Write module


def write(mesh, file_name):
    # TODO: check that mesh is meshio.Mesh
    mesh._mesh.write(file_name)
    pass
