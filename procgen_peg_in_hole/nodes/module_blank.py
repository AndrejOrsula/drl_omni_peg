def assemblymoduleblank_node_group():
    assemblymoduleblank = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="AssemblyModuleBlank"
    )

    frame = assemblymoduleblank.nodes.new("NodeFrame")
    frame.label = "Module (1x1)"

    frame_001 = assemblymoduleblank.nodes.new("NodeFrame")
    frame_001.label = "Extend to MxN modules"

    frame_002 = assemblymoduleblank.nodes.new("NodeFrame")
    frame_002.label = "Tolerance (reduce module size in XY plane)"

    frame_003 = assemblymoduleblank.nodes.new("NodeFrame")
    frame_003.label = "Holes (if enabled)"

    frame_004 = assemblymoduleblank.nodes.new("NodeFrame")
    frame_004.label = "Set origin to module centre (if enabled)"

    frame_005 = assemblymoduleblank.nodes.new("NodeFrame")
    frame_005.label = "Set origin to the bottom of the module"

    frame_006 = assemblymoduleblank.nodes.new("NodeFrame")
    frame_006.label = "UV"

    transform_geometry = assemblymoduleblank.nodes.new("GeometryNodeTransform")
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    assemblymoduleblank.inputs.new("NodeSocketBool", "module_centering")
    assemblymoduleblank.inputs[0].default_value = True
    assemblymoduleblank.inputs[0].attribute_domain = "POINT"

    assemblymoduleblank.inputs.new("NodeSocketFloatDistance", "module_size")
    assemblymoduleblank.inputs[1].default_value = 0.15000000596046448
    assemblymoduleblank.inputs[1].min_value = 0.0
    assemblymoduleblank.inputs[1].max_value = 3.4028234663852886e38
    assemblymoduleblank.inputs[1].attribute_domain = "POINT"
    assemblymoduleblank.inputs[1].description = (
        "Size of a single square module in the XY plane"
    )

    assemblymoduleblank.inputs.new("NodeSocketFloatDistance", "module_thickness")
    assemblymoduleblank.inputs[2].default_value = 0.003000000026077032
    assemblymoduleblank.inputs[2].min_value = 0.0
    assemblymoduleblank.inputs[2].max_value = 3.4028234663852886e38
    assemblymoduleblank.inputs[2].attribute_domain = "POINT"
    assemblymoduleblank.inputs[2].description = "Thickness of module along Z axis"

    assemblymoduleblank.inputs.new("NodeSocketFloatDistance", "module_size_tolerance")
    assemblymoduleblank.inputs[3].default_value = 0.0010000000474974513
    assemblymoduleblank.inputs[3].min_value = 0.0
    assemblymoduleblank.inputs[3].max_value = 3.4028234663852886e38
    assemblymoduleblank.inputs[3].attribute_domain = "POINT"

    assemblymoduleblank.inputs.new("NodeSocketInt", "module_count_x")
    assemblymoduleblank.inputs[4].default_value = 1
    assemblymoduleblank.inputs[4].min_value = 1
    assemblymoduleblank.inputs[4].max_value = 2147483647
    assemblymoduleblank.inputs[4].attribute_domain = "POINT"
    assemblymoduleblank.inputs[4].description = (
        "Number of combined module plates along X axis"
    )

    assemblymoduleblank.inputs.new("NodeSocketInt", "module_count_y")
    assemblymoduleblank.inputs[5].default_value = 1
    assemblymoduleblank.inputs[5].min_value = 1
    assemblymoduleblank.inputs[5].max_value = 2147483647
    assemblymoduleblank.inputs[5].attribute_domain = "POINT"
    assemblymoduleblank.inputs[5].description = (
        "Number of combined module plates along Y axis"
    )

    assemblymoduleblank.inputs.new("NodeSocketBool", "holes_enable")
    assemblymoduleblank.inputs[6].default_value = False
    assemblymoduleblank.inputs[6].attribute_domain = "POINT"

    assemblymoduleblank.inputs.new("NodeSocketInt", "holes_vertices")
    assemblymoduleblank.inputs[7].default_value = 16
    assemblymoduleblank.inputs[7].min_value = 3
    assemblymoduleblank.inputs[7].max_value = 2147483647
    assemblymoduleblank.inputs[7].attribute_domain = "POINT"

    assemblymoduleblank.inputs.new(
        "NodeSocketFloatDistance", "holes_offset_from_corner"
    )
    assemblymoduleblank.inputs[8].default_value = 0.014999999664723873
    assemblymoduleblank.inputs[8].min_value = 0.0
    assemblymoduleblank.inputs[8].max_value = 3.4028234663852886e38
    assemblymoduleblank.inputs[8].attribute_domain = "POINT"

    assemblymoduleblank.inputs.new("NodeSocketFloatDistance", "holes_diameter")
    assemblymoduleblank.inputs[9].default_value = 0.00430000014603138
    assemblymoduleblank.inputs[9].min_value = 0.0
    assemblymoduleblank.inputs[9].max_value = 3.4028234663852886e38
    assemblymoduleblank.inputs[9].attribute_domain = "POINT"

    group_input = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input.outputs[0].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True
    group_input.outputs[7].hide = True
    group_input.outputs[8].hide = True
    group_input.outputs[9].hide = True
    group_input.outputs[10].hide = True

    cube = assemblymoduleblank.nodes.new("GeometryNodeMeshCube")
    cube.inputs[1].default_value = 2
    cube.inputs[2].default_value = 2
    cube.inputs[3].default_value = 2

    combine_xyz = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")

    combine_xyz_001 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.inputs[2].hide = True
    combine_xyz_001.inputs[2].default_value = 0.0

    group_input_001 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True

    math = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math.operation = "MULTIPLY"
    math.inputs[1].default_value = 0.5
    math.inputs[2].default_value = 0.5

    normal = assemblymoduleblank.nodes.new("GeometryNodeInputNormal")

    separate_xyz = assemblymoduleblank.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.outputs[2].hide = True

    compare = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare.data_type = "FLOAT"
    compare.operation = "GREATER_THAN"
    compare.mode = "ELEMENT"
    compare.inputs[1].default_value = 0.0
    compare.inputs[2].default_value = 0
    compare.inputs[3].default_value = 0
    compare.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare.inputs[8].default_value = ""
    compare.inputs[9].default_value = ""
    compare.inputs[10].default_value = 0.8999999761581421
    compare.inputs[11].default_value = 0.08726649731397629
    compare.inputs[12].default_value = 0.0010000000474974513

    group_input_002 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True

    math_001 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_001.operation = "ADD"
    math_001.inputs[1].default_value = -1.0
    math_001.inputs[2].default_value = 0.5

    combine_xyz_002 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[2].hide = True
    combine_xyz_002.inputs[0].default_value = 0.0
    combine_xyz_002.inputs[2].default_value = 0.0

    math_002 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_002.operation = "MULTIPLY"
    math_002.inputs[2].hide = True
    math_002.inputs[2].default_value = 0.5

    math_003 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_003.operation = "MULTIPLY"
    math_003.inputs[2].default_value = 0.5

    math_004 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_004.operation = "ADD"
    math_004.inputs[1].default_value = -1.0
    math_004.inputs[2].default_value = 0.5

    group_input_003 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True

    combine_xyz_003 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.inputs[1].hide = True
    combine_xyz_003.inputs[2].hide = True
    combine_xyz_003.inputs[1].default_value = 0.0
    combine_xyz_003.inputs[2].default_value = 0.0

    compare_001 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_001.data_type = "FLOAT"
    compare_001.operation = "GREATER_THAN"
    compare_001.mode = "ELEMENT"
    compare_001.inputs[1].default_value = 0.0
    compare_001.inputs[2].default_value = 0
    compare_001.inputs[3].default_value = 0
    compare_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_001.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_001.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_001.inputs[8].default_value = ""
    compare_001.inputs[9].default_value = ""
    compare_001.inputs[10].default_value = 0.8999999761581421
    compare_001.inputs[11].default_value = 0.08726649731397629
    compare_001.inputs[12].default_value = 0.0010000000474974513

    set_position = assemblymoduleblank.nodes.new("GeometryNodeSetPosition")
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    set_position_001 = assemblymoduleblank.nodes.new("GeometryNodeSetPosition")
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    set_position_002 = assemblymoduleblank.nodes.new("GeometryNodeSetPosition")
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    set_position_003 = assemblymoduleblank.nodes.new("GeometryNodeSetPosition")
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    combine_xyz_004 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.inputs[0].hide = True
    combine_xyz_004.inputs[2].hide = True
    combine_xyz_004.inputs[0].default_value = 0.0
    combine_xyz_004.inputs[2].default_value = 0.0

    combine_xyz_005 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.inputs[0].hide = True
    combine_xyz_005.inputs[2].hide = True
    combine_xyz_005.inputs[0].default_value = 0.0
    combine_xyz_005.inputs[2].default_value = 0.0

    math_005 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_005.operation = "MULTIPLY"
    math_005.inputs[1].default_value = -1.0
    math_005.inputs[2].default_value = 0.5

    group_input_004 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True

    compare_002 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_002.data_type = "FLOAT"
    compare_002.operation = "GREATER_THAN"
    compare_002.mode = "ELEMENT"
    compare_002.inputs[1].default_value = 0.0
    compare_002.inputs[2].default_value = 0
    compare_002.inputs[3].default_value = 0
    compare_002.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_002.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_002.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_002.inputs[8].default_value = ""
    compare_002.inputs[9].default_value = ""
    compare_002.inputs[10].default_value = 0.8999999761581421
    compare_002.inputs[11].default_value = 0.08726649731397629
    compare_002.inputs[12].default_value = 0.0010000000474974513

    compare_003 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_003.data_type = "FLOAT"
    compare_003.operation = "LESS_THAN"
    compare_003.mode = "ELEMENT"
    compare_003.inputs[1].default_value = 0.0
    compare_003.inputs[2].default_value = 0
    compare_003.inputs[3].default_value = 0
    compare_003.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare_003.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_003.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_003.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_003.inputs[8].default_value = ""
    compare_003.inputs[9].default_value = ""
    compare_003.inputs[10].default_value = 0.8999999761581421
    compare_003.inputs[11].default_value = 0.08726649731397629
    compare_003.inputs[12].default_value = 0.0010000000474974513

    separate_xyz_001 = assemblymoduleblank.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.outputs[0].hide = True
    separate_xyz_001.outputs[2].hide = True

    normal_001 = assemblymoduleblank.nodes.new("GeometryNodeInputNormal")

    separate_xyz_002 = assemblymoduleblank.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.outputs[1].hide = True
    separate_xyz_002.outputs[2].hide = True

    compare_004 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_004.data_type = "FLOAT"
    compare_004.operation = "LESS_THAN"
    compare_004.mode = "ELEMENT"
    compare_004.inputs[1].default_value = 0.0
    compare_004.inputs[2].default_value = 0
    compare_004.inputs[3].default_value = 0
    compare_004.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare_004.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_004.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_004.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_004.inputs[8].default_value = ""
    compare_004.inputs[9].default_value = ""
    compare_004.inputs[10].default_value = 0.8999999761581421
    compare_004.inputs[11].default_value = 0.08726649731397629
    compare_004.inputs[12].default_value = 0.0010000000474974513

    compare_005 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_005.data_type = "FLOAT"
    compare_005.operation = "GREATER_THAN"
    compare_005.mode = "ELEMENT"
    compare_005.inputs[1].default_value = 0.0
    compare_005.inputs[2].default_value = 0
    compare_005.inputs[3].default_value = 0
    compare_005.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare_005.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_005.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_005.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_005.inputs[8].default_value = ""
    compare_005.inputs[9].default_value = ""
    compare_005.inputs[10].default_value = 0.8999999761581421
    compare_005.inputs[11].default_value = 0.08726649731397629
    compare_005.inputs[12].default_value = 0.0010000000474974513

    group_input_005 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True

    math_006 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_006.operation = "MULTIPLY"
    math_006.inputs[1].default_value = -1.0
    math_006.inputs[2].default_value = 0.5

    combine_xyz_006 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.inputs[1].hide = True
    combine_xyz_006.inputs[2].hide = True
    combine_xyz_006.inputs[1].default_value = 0.0
    combine_xyz_006.inputs[2].default_value = 0.0

    combine_xyz_007 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.inputs[1].hide = True
    combine_xyz_007.inputs[2].hide = True
    combine_xyz_007.inputs[1].default_value = 0.0
    combine_xyz_007.inputs[2].default_value = 0.0

    set_position_004 = assemblymoduleblank.nodes.new("GeometryNodeSetPosition")
    set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)

    set_position_005 = assemblymoduleblank.nodes.new("GeometryNodeSetPosition")
    set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)

    instance_on_points = assemblymoduleblank.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.inputs[3].hide = True
    instance_on_points.inputs[4].hide = True
    instance_on_points.inputs[5].hide = True
    instance_on_points.inputs[6].hide = True
    instance_on_points.inputs[3].default_value = False
    instance_on_points.inputs[4].default_value = 0
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    group_input_006 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True

    realize_instances = assemblymoduleblank.nodes.new("GeometryNodeRealizeInstances")

    merge_by_distance = assemblymoduleblank.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.mode = "ALL"
    merge_by_distance.inputs[1].default_value = True
    merge_by_distance.inputs[2].default_value = 9.999999747378752e-05

    mesh_to_points = assemblymoduleblank.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points.mode = "VERTICES"
    mesh_to_points.inputs[1].default_value = True
    mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points.inputs[3].default_value = 0.05000000074505806

    mesh_to_points_001 = assemblymoduleblank.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_001.mode = "VERTICES"
    mesh_to_points_001.inputs[1].default_value = True
    mesh_to_points_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_001.inputs[3].default_value = 0.05000000074505806

    instance_on_points_001 = assemblymoduleblank.nodes.new(
        "GeometryNodeInstanceOnPoints"
    )
    instance_on_points_001.inputs[1].hide = True
    instance_on_points_001.inputs[3].hide = True
    instance_on_points_001.inputs[4].hide = True
    instance_on_points_001.inputs[5].hide = True
    instance_on_points_001.inputs[6].hide = True
    instance_on_points_001.inputs[1].default_value = True
    instance_on_points_001.inputs[3].default_value = False
    instance_on_points_001.inputs[4].default_value = 0
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

    instance_on_points_002 = assemblymoduleblank.nodes.new(
        "GeometryNodeInstanceOnPoints"
    )
    instance_on_points_002.inputs[1].hide = True
    instance_on_points_002.inputs[3].hide = True
    instance_on_points_002.inputs[4].hide = True
    instance_on_points_002.inputs[5].hide = True
    instance_on_points_002.inputs[6].hide = True
    instance_on_points_002.inputs[1].default_value = True
    instance_on_points_002.inputs[3].default_value = False
    instance_on_points_002.inputs[4].default_value = 0
    instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)

    transform_geometry_001 = assemblymoduleblank.nodes.new("GeometryNodeTransform")
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    transform_geometry_002 = assemblymoduleblank.nodes.new("GeometryNodeTransform")
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    group_input_007 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True

    math_007 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_007.operation = "MULTIPLY"
    math_007.inputs[2].default_value = 0.5

    math_008 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_008.operation = "MULTIPLY"
    math_008.inputs[1].default_value = 2.0
    math_008.inputs[2].default_value = 0.5

    math_009 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_009.operation = "SUBTRACT"
    math_009.inputs[2].default_value = 0.5

    group_input_008 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True

    math_010 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_010.operation = "MULTIPLY"
    math_010.inputs[2].default_value = 0.5

    math_011 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_011.operation = "MULTIPLY"
    math_011.inputs[1].default_value = 2.0
    math_011.inputs[2].default_value = 0.5

    math_012 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_012.operation = "SUBTRACT"
    math_012.inputs[2].default_value = 0.5

    combine_xyz_008 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.inputs[0].hide = True
    combine_xyz_008.inputs[2].hide = True
    combine_xyz_008.inputs[0].default_value = 0.0
    combine_xyz_008.inputs[2].default_value = 0.0

    combine_xyz_009 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_009.inputs[1].hide = True
    combine_xyz_009.inputs[2].hide = True
    combine_xyz_009.inputs[1].default_value = 0.0
    combine_xyz_009.inputs[2].default_value = 0.0

    duplicate_elements = assemblymoduleblank.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements.domain = "POINT"
    duplicate_elements.inputs[1].default_value = True
    duplicate_elements.inputs[2].default_value = 1

    group_input_009 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True

    math_013 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_013.operation = "SUBTRACT"
    math_013.inputs[2].default_value = 0.5

    points = assemblymoduleblank.nodes.new("GeometryNodePoints")
    points.inputs[0].default_value = 1
    points.inputs[2].default_value = 0.05000000074505806

    points_001 = assemblymoduleblank.nodes.new("GeometryNodePoints")
    points_001.inputs[0].default_value = 1
    points_001.inputs[2].default_value = 0.05000000074505806

    math_014 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_014.operation = "MULTIPLY"
    math_014.inputs[1].default_value = 2.0
    math_014.inputs[2].default_value = 0.5

    combine_xyz_010 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_010.inputs[0].hide = True
    combine_xyz_010.inputs[2].hide = True
    combine_xyz_010.inputs[0].default_value = 0.0
    combine_xyz_010.inputs[2].default_value = 0.0

    combine_xyz_011 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_011.inputs[1].hide = True
    combine_xyz_011.inputs[2].hide = True
    combine_xyz_011.inputs[1].default_value = 0.0
    combine_xyz_011.inputs[2].default_value = 0.0

    points_002 = assemblymoduleblank.nodes.new("GeometryNodePoints")
    points_002.inputs[0].default_value = 1
    points_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    points_002.inputs[2].default_value = 0.05000000074505806

    join_geometry = assemblymoduleblank.nodes.new("GeometryNodeJoinGeometry")

    transform_geometry_003 = assemblymoduleblank.nodes.new("GeometryNodeTransform")
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    transform_geometry_004 = assemblymoduleblank.nodes.new("GeometryNodeTransform")
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[3].hide = True
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    combine_xyz_012 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_012.inputs[2].hide = True
    combine_xyz_012.inputs[2].default_value = 0.0

    mesh_line = assemblymoduleblank.nodes.new("GeometryNodeMeshLine")
    mesh_line.mode = "OFFSET"
    mesh_line.inputs[1].default_value = 1.0
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)

    mesh_line_001 = assemblymoduleblank.nodes.new("GeometryNodeMeshLine")
    mesh_line_001.mode = "OFFSET"
    mesh_line_001.inputs[1].default_value = 1.0
    mesh_line_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    combine_xyz_013 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_013.inputs[1].hide = True
    combine_xyz_013.inputs[2].hide = True
    combine_xyz_013.inputs[1].default_value = 0.0
    combine_xyz_013.inputs[2].default_value = 0.0

    combine_xyz_014 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_014.inputs[0].hide = True
    combine_xyz_014.inputs[2].hide = True
    combine_xyz_014.inputs[0].default_value = 0.0
    combine_xyz_014.inputs[2].default_value = 0.0

    group_input_010 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True

    duplicate_elements_001 = assemblymoduleblank.nodes.new(
        "GeometryNodeDuplicateElements"
    )
    duplicate_elements_001.domain = "POINT"
    duplicate_elements_001.inputs[1].default_value = True
    duplicate_elements_001.inputs[2].default_value = 1

    join_geometry_001 = assemblymoduleblank.nodes.new("GeometryNodeJoinGeometry")

    join_geometry_002 = assemblymoduleblank.nodes.new("GeometryNodeJoinGeometry")

    math_015 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_015.operation = "MULTIPLY"
    math_015.inputs[2].default_value = 0.5

    math_016 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_016.operation = "MULTIPLY"
    math_016.inputs[2].default_value = 0.5

    group_input_011 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True

    math_017 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_017.operation = "MULTIPLY"
    math_017.inputs[1].default_value = -0.5
    math_017.inputs[2].default_value = 0.5

    math_018 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_018.operation = "MULTIPLY"
    math_018.inputs[1].default_value = -0.5
    math_018.inputs[2].default_value = 0.5

    combine_xyz_015 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_015.inputs[2].hide = True
    combine_xyz_015.inputs[2].default_value = 0.0

    vector_math = assemblymoduleblank.nodes.new("ShaderNodeVectorMath")
    vector_math.operation = "MULTIPLY"
    vector_math.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math.inputs[3].default_value = 1.0

    group_input_012 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True

    math_019 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_019.operation = "MULTIPLY"
    math_019.inputs[1].default_value = 0.5
    math_019.inputs[2].default_value = 0.5

    combine_xyz_016 = assemblymoduleblank.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_016.inputs[0].hide = True
    combine_xyz_016.inputs[1].hide = True
    combine_xyz_016.inputs[0].default_value = 0.0
    combine_xyz_016.inputs[1].default_value = 0.0

    group_input_013 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True

    vector_math_001 = assemblymoduleblank.nodes.new("ShaderNodeVectorMath")
    vector_math_001.operation = "ADD"
    vector_math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_001.inputs[3].default_value = 1.0

    mesh_boolean = assemblymoduleblank.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.operation = "DIFFERENCE"
    mesh_boolean.inputs[2].default_value = False
    mesh_boolean.inputs[3].default_value = False

    math_020 = assemblymoduleblank.nodes.new("ShaderNodeMath")
    math_020.operation = "MULTIPLY"
    math_020.inputs[1].default_value = 0.5
    math_020.inputs[2].default_value = 0.5

    group_input_014 = assemblymoduleblank.nodes.new("NodeGroupInput")
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[10].hide = True

    compare_006 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_006.data_type = "FLOAT"
    compare_006.operation = "EQUAL"
    compare_006.mode = "ELEMENT"
    compare_006.inputs[1].default_value = 1.0
    compare_006.inputs[2].default_value = 0
    compare_006.inputs[3].default_value = 0
    compare_006.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare_006.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_006.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_006.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_006.inputs[8].default_value = ""
    compare_006.inputs[9].default_value = ""
    compare_006.inputs[10].default_value = 0.8999999761581421
    compare_006.inputs[11].default_value = 0.08726649731397629
    compare_006.inputs[12].default_value = 0.0

    separate_xyz_003 = assemblymoduleblank.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.outputs[1].hide = True
    separate_xyz_003.outputs[2].hide = True

    normal_002 = assemblymoduleblank.nodes.new("GeometryNodeInputNormal")

    geometry_to_instance = assemblymoduleblank.nodes.new(
        "GeometryNodeGeometryToInstance"
    )

    transform_geometry_005 = assemblymoduleblank.nodes.new("GeometryNodeTransform")
    transform_geometry_005.inputs[2].hide = True
    transform_geometry_005.inputs[3].hide = True
    transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)

    assemblymoduleblank.outputs.new("NodeSocketGeometry", "Geometry")
    assemblymoduleblank.outputs[0].attribute_domain = "POINT"

    assemblymoduleblank.outputs.new("NodeSocketVector", "UV Map")
    assemblymoduleblank.outputs[1].default_value = (0.0, 0.0, 0.0)
    assemblymoduleblank.outputs[1].min_value = -3.4028234663852886e38
    assemblymoduleblank.outputs[1].max_value = 3.4028234663852886e38
    assemblymoduleblank.outputs[1].default_attribute_name = "UV Map"
    assemblymoduleblank.outputs[1].attribute_domain = "POINT"

    group_output = assemblymoduleblank.nodes.new("NodeGroupOutput")

    store_named_attribute = assemblymoduleblank.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute.data_type = "BOOLEAN"
    store_named_attribute.domain = "EDGE"
    store_named_attribute.inputs[2].default_value = "seam_holes"
    store_named_attribute.inputs[3].default_value = (0.0, 0.0, 0.0)
    store_named_attribute.inputs[4].default_value = 0.0
    store_named_attribute.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
    store_named_attribute.inputs[6].default_value = True
    store_named_attribute.inputs[7].default_value = 0

    named_attribute = assemblymoduleblank.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.data_type = "BOOLEAN"
    named_attribute.inputs[0].default_value = "seam_holes"

    edge_angle = assemblymoduleblank.nodes.new("GeometryNodeInputMeshEdgeAngle")
    edge_angle.outputs[1].hide = True

    compare_007 = assemblymoduleblank.nodes.new("FunctionNodeCompare")
    compare_007.data_type = "FLOAT"
    compare_007.operation = "EQUAL"
    compare_007.mode = "ELEMENT"
    compare_007.inputs[1].default_value = 1.5707963705062866
    compare_007.inputs[2].default_value = 0
    compare_007.inputs[3].default_value = 0
    compare_007.inputs[4].default_value = (0.0, 0.0, 0.0)
    compare_007.inputs[5].default_value = (0.0, 0.0, 0.0)
    compare_007.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_007.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_007.inputs[8].default_value = ""
    compare_007.inputs[9].default_value = ""
    compare_007.inputs[10].default_value = 0.8999999761581421
    compare_007.inputs[11].default_value = 0.08726649731397629
    compare_007.inputs[12].default_value = 0.0010000000474974513

    boolean_math = assemblymoduleblank.nodes.new("FunctionNodeBooleanMath")
    boolean_math.operation = "OR"

    uv_unwrap = assemblymoduleblank.nodes.new("GeometryNodeUVUnwrap")
    uv_unwrap.method = "ANGLE_BASED"
    uv_unwrap.inputs[0].default_value = True
    uv_unwrap.inputs[2].default_value = 0.0
    uv_unwrap.inputs[3].default_value = False

    cylinder = assemblymoduleblank.nodes.new("GeometryNodeMeshCylinder")
    cylinder.fill_type = "NONE"
    cylinder.inputs[1].default_value = 1
    cylinder.inputs[2].default_value = 1

    set_shade_smooth = assemblymoduleblank.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.inputs[2].default_value = True

    join_geometry_003 = assemblymoduleblank.nodes.new("GeometryNodeJoinGeometry")

    transform_geometry.parent = frame
    group_input.parent = frame
    cube.parent = frame
    combine_xyz.parent = frame
    combine_xyz_001.parent = frame
    group_input_001.parent = frame
    math.parent = frame
    normal.parent = frame_001
    separate_xyz.parent = frame_001
    compare.parent = frame_001
    group_input_002.parent = frame_001
    math_001.parent = frame_001
    combine_xyz_002.parent = frame_001
    math_002.parent = frame_001
    math_003.parent = frame_001
    math_004.parent = frame_001
    group_input_003.parent = frame_001
    combine_xyz_003.parent = frame_001
    compare_001.parent = frame_001
    set_position.parent = frame_001
    set_position_001.parent = frame_001
    set_position_002.parent = frame_002
    set_position_003.parent = frame_002
    combine_xyz_004.parent = frame_002
    combine_xyz_005.parent = frame_002
    math_005.parent = frame_002
    group_input_004.parent = frame_002
    compare_002.parent = frame_002
    compare_003.parent = frame_002
    separate_xyz_001.parent = frame_002
    normal_001.parent = frame_002
    separate_xyz_002.parent = frame_002
    compare_004.parent = frame_002
    compare_005.parent = frame_002
    group_input_005.parent = frame_002
    math_006.parent = frame_002
    combine_xyz_006.parent = frame_002
    combine_xyz_007.parent = frame_002
    set_position_004.parent = frame_002
    set_position_005.parent = frame_002
    instance_on_points.parent = frame_003
    group_input_006.parent = frame_003
    realize_instances.parent = frame_003
    merge_by_distance.parent = frame_003
    mesh_to_points.parent = frame_003
    mesh_to_points_001.parent = frame_003
    instance_on_points_001.parent = frame_003
    instance_on_points_002.parent = frame_003
    transform_geometry_001.parent = frame_003
    transform_geometry_002.parent = frame_003
    group_input_007.parent = frame_003
    math_007.parent = frame_003
    math_008.parent = frame_003
    math_009.parent = frame_003
    group_input_008.parent = frame_003
    math_010.parent = frame_003
    math_011.parent = frame_003
    math_012.parent = frame_003
    combine_xyz_008.parent = frame_003
    combine_xyz_009.parent = frame_003
    duplicate_elements.parent = frame_003
    group_input_009.parent = frame_003
    math_013.parent = frame_003
    points.parent = frame_003
    points_001.parent = frame_003
    math_014.parent = frame_003
    combine_xyz_010.parent = frame_003
    combine_xyz_011.parent = frame_003
    points_002.parent = frame_003
    join_geometry.parent = frame_003
    transform_geometry_003.parent = frame_003
    transform_geometry_004.parent = frame_003
    combine_xyz_012.parent = frame_003
    mesh_line.parent = frame_003
    mesh_line_001.parent = frame_003
    combine_xyz_013.parent = frame_003
    combine_xyz_014.parent = frame_003
    group_input_010.parent = frame_003
    duplicate_elements_001.parent = frame_003
    join_geometry_001.parent = frame_003
    join_geometry_002.parent = frame_003
    math_015.parent = frame_004
    math_016.parent = frame_004
    group_input_011.parent = frame_004
    math_017.parent = frame_004
    math_018.parent = frame_004
    combine_xyz_015.parent = frame_004
    vector_math.parent = frame_004
    group_input_012.parent = frame_004
    math_019.parent = frame_005
    combine_xyz_016.parent = frame_005
    group_input_013.parent = frame_005
    vector_math_001.parent = frame_005
    mesh_boolean.parent = frame_003
    math_020.parent = frame_003
    group_input_014.parent = frame_003
    compare_006.parent = frame_003
    separate_xyz_003.parent = frame_003
    normal_002.parent = frame_003
    geometry_to_instance.parent = frame_003
    store_named_attribute.parent = frame_003
    named_attribute.parent = frame_006
    edge_angle.parent = frame_006
    compare_007.parent = frame_006
    boolean_math.parent = frame_006
    uv_unwrap.parent = frame_006
    cylinder.parent = frame_003
    set_shade_smooth.parent = frame_003
    join_geometry_003.parent = frame_003

    frame.location = (-8184.921875, 2045.48828125)
    frame_001.location = (-5897.60546875, 2412.5478515625)
    frame_002.location = (-5793.84423828125, 2441.30322265625)
    frame_003.location = (-444.615234375, 1014.5482788085938)
    frame_004.location = (-530.7978515625, 220.8665771484375)
    frame_005.location = (-608.75244140625, 317.6299743652344)
    frame_006.location = (1477.7294921875, 112.75860595703125)
    transform_geometry.location = (-632.6036376953125, 45.062469482421875)
    group_input.location = (-1202.6036376953125, 32.562469482421875)
    cube.location = (-822.6036376953125, 77.06246948242188)
    combine_xyz.location = (-1012.6036376953125, 55.062469482421875)
    combine_xyz_001.location = (-818.9298095703125, -152.18344116210938)
    group_input_001.location = (-1198.9298095703125, -175.68344116210938)
    math.location = (-1008.9298095703125, -124.6834487915039)
    normal.location = (-2600.792236328125, -688.3894653320312)
    separate_xyz.location = (-2410.792236328125, -663.8894653320312)
    compare.location = (-2202.9609375, -691.4400024414062)
    group_input_002.location = (-1986.91650390625, -769.8660888671875)
    math_001.location = (-1796.91650390625, -729.8660888671875)
    combine_xyz_002.location = (-1416.91650390625, -768.3660888671875)
    math_002.location = (-1606.91650390625, -729.8660888671875)
    math_003.location = (-1602.591796875, -519.2313232421875)
    math_004.location = (-1792.591796875, -519.2313232421875)
    group_input_003.location = (-1982.591796875, -559.2313232421875)
    combine_xyz_003.location = (-1412.591796875, -557.7313232421875)
    compare_001.location = (-2202.9609375, -522.4400024414062)
    set_position.location = (-1199.119384765625, -285.128173828125)
    set_position_001.location = (-950.6165161132812, -579.2698974609375)
    set_position_002.location = (1901.6348876953125, -1149.798095703125)
    set_position_003.location = (1685.6138916015625, -881.1987915039062)
    combine_xyz_004.location = (1484.8563232421875, -1016.313232421875)
    combine_xyz_005.location = (1484.8563232421875, -1143.90771484375)
    math_005.location = (1288.50830078125, -1038.09423828125)
    group_input_004.location = (1093.5130615234375, -1161.686279296875)
    compare_002.location = (907.4673461914062, -1027.34765625)
    compare_003.location = (907.4673461914062, -1196.34765625)
    separate_xyz_001.location = (715.796142578125, -1170.029541015625)
    normal_001.location = (-706.6566162109375, -1023.052978515625)
    separate_xyz_002.location = (-472.5413513183594, -866.019775390625)
    compare_004.location = (-280.8701477050781, -892.3379516601562)
    compare_005.location = (-280.8701477050781, -723.337890625)
    group_input_005.location = (-94.82441711425781, -857.676513671875)
    math_006.location = (100.17082214355469, -734.08447265625)
    combine_xyz_006.location = (296.5188293457031, -839.89794921875)
    combine_xyz_007.location = (296.5188293457031, -712.303466796875)
    set_position_004.location = (497.2763977050781, -577.1890869140625)
    set_position_005.location = (713.2974243164062, -845.788330078125)
    instance_on_points.location = (-3476.369140625, -1264.945556640625)
    group_input_006.location = (-3797.7763671875, -1308.520751953125)
    realize_instances.location = (-4827.376953125, -879.7869873046875)
    merge_by_distance.location = (-4637.376953125, -842.7869873046875)
    mesh_to_points.location = (-6536.9853515625, -649.318603515625)
    mesh_to_points_001.location = (-6535.70166015625, -1161.8203125)
    instance_on_points_001.location = (-6352.9990234375, -483.599365234375)
    instance_on_points_002.location = (-6352.9990234375, -1325.7928466796875)
    transform_geometry_001.location = (-5339.39794921875, -402.599365234375)
    transform_geometry_002.location = (-5339.39794921875, -1244.7928466796875)
    group_input_007.location = (-6144.2470703125, -629.9935302734375)
    math_007.location = (-5954.2470703125, -550.1070556640625)
    math_008.location = (-5951.7841796875, -720.726318359375)
    math_009.location = (-5728.86572265625, -627.933349609375)
    group_input_008.location = (-6142.41357421875, -1407.496826171875)
    math_010.location = (-5952.41357421875, -1327.6103515625)
    math_011.location = (-5949.951171875, -1498.2296142578125)
    math_012.location = (-5727.0322265625, -1405.4366455078125)
    combine_xyz_008.location = (-5532.04443359375, -1406.0213623046875)
    combine_xyz_009.location = (-5533.8779296875, -628.5179443359375)
    duplicate_elements.location = (-5602.50048828125, -1182.634521484375)
    group_input_009.location = (-8944.658203125, -1104.2965087890625)
    math_013.location = (-8488.068359375, -1026.1923828125)
    points.location = (-7983.822265625, -1082.4669189453125)
    points_001.location = (-7983.822265625, -948.4669189453125)
    math_014.location = (-8724.419921875, -1199.1781005859375)
    combine_xyz_010.location = (-8221.30078125, -995.046142578125)
    combine_xyz_011.location = (-8221.30078125, -1127.0455322265625)
    points_002.location = (-7983.822265625, -720.71728515625)
    join_geometry.location = (-7760.1640625, -1061.3992919921875)
    transform_geometry_003.location = (-7495.4501953125, -900.9609375)
    transform_geometry_004.location = (-7495.4501953125, -1035.23095703125)
    combine_xyz_012.location = (-7760.4423828125, -1207.90234375)
    mesh_line.location = (-6726.9853515625, -780.756591796875)
    mesh_line_001.location = (-6725.7021484375, -1024.68505859375)
    combine_xyz_013.location = (-6915.7021484375, -1110.3203125)
    combine_xyz_014.location = (-6916.65283203125, -920.182373046875)
    group_input_010.location = (-7114.283203125, -981.017822265625)
    duplicate_elements_001.location = (-5602.50048828125, -340.4410400390625)
    join_geometry_001.location = (-5017.376953125, -874.7869873046875)
    join_geometry_002.location = (-6112.875, -908.308837890625)
    math_015.location = (-1634.18310546875, -509.2121276855469)
    math_016.location = (-1634.18310546875, -340.2121276855469)
    group_input_011.location = (-1836.93603515625, -470.1422119140625)
    math_017.location = (-1456.55908203125, -508.96429443359375)
    math_018.location = (-1456.55908203125, -339.96429443359375)
    combine_xyz_015.location = (-1208.8779296875, -456.9739074707031)
    vector_math.location = (-1012.79833984375, -386.2425842285156)
    group_input_012.location = (-1212.09765625, -387.7550354003906)
    math_019.location = (-926.01953125, -149.020263671875)
    combine_xyz_016.location = (-751.80712890625, -131.4840087890625)
    group_input_013.location = (-1102.30224609375, -227.88442993164062)
    vector_math_001.location = (-505.8935546875, -193.17498779296875)
    mesh_boolean.location = (-2533.68994140625, -626.8739013671875)
    math_020.location = (-5413.71044921875, -1934.98095703125)
    group_input_014.location = (-5593.56103515625, -1769.2479248046875)
    compare_006.location = (-4549.70556640625, -1834.489013671875)
    separate_xyz_003.location = (-4739.70556640625, -1882.989013671875)
    normal_002.location = (-4929.70556640625, -1896.489013671875)
    geometry_to_instance.location = (-3925.556884765625, -1573.0072021484375)
    transform_geometry_005.location = (-724.41845703125, 409.9898376464844)
    group_output.location = (1108.9892578125, 403.5124206542969)
    store_named_attribute.location = (-4323.96484375, -1700.503173828125)
    named_attribute.location = (-1488.96826171875, -138.58251953125)
    edge_angle.location = (-1693.16845703125, -33.33734130859375)
    compare_007.location = (-1488.494140625, 47.50390625)
    boolean_math.location = (-1185.81103515625, 7.9971923828125)
    uv_unwrap.location = (-984.39453125, 82.75079345703125)
    cylinder.location = (-5150.81787109375, -1749.5826416015625)
    set_shade_smooth.location = (-4737.7041015625, -1735.38330078125)
    join_geometry_003.location = (-7760.1640625, -925.5980224609375)

    frame.width, frame.height = 770.0, 426.0
    frame_001.width, frame_001.height = 1850.0, 668.0
    frame_002.width, frame_002.height = 2809.0, 843.0
    frame_003.width, frame_003.height = 6611.0, 1818.0
    frame_004.width, frame_004.height = 1024.0, 393.0
    frame_005.width, frame_005.height = 796.0, 263.0
    frame_006.width, frame_006.height = 908.0, 419.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    compare_005.width, compare_005.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
    combine_xyz_007.width, combine_xyz_007.height = 140.0, 100.0
    set_position_004.width, set_position_004.height = 140.0, 100.0
    set_position_005.width, set_position_005.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
    mesh_to_points_001.width, mesh_to_points_001.height = 140.0, 100.0
    instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
    instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    combine_xyz_008.width, combine_xyz_008.height = 140.0, 100.0
    combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
    duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    points.width, points.height = 140.0, 100.0
    points_001.width, points_001.height = 140.0, 100.0
    math_014.width, math_014.height = 140.0, 100.0
    combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
    combine_xyz_011.width, combine_xyz_011.height = 140.0, 100.0
    points_002.width, points_002.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    combine_xyz_012.width, combine_xyz_012.height = 140.0, 100.0
    mesh_line.width, mesh_line.height = 140.0, 100.0
    mesh_line_001.width, mesh_line_001.height = 140.0, 100.0
    combine_xyz_013.width, combine_xyz_013.height = 140.0, 100.0
    combine_xyz_014.width, combine_xyz_014.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    duplicate_elements_001.width, duplicate_elements_001.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
    math_015.width, math_015.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    combine_xyz_015.width, combine_xyz_015.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    math_019.width, math_019.height = 140.0, 100.0
    combine_xyz_016.width, combine_xyz_016.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    math_020.width, math_020.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    compare_006.width, compare_006.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
    transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 166.968994140625, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    edge_angle.width, edge_angle.height = 140.0, 100.0
    compare_007.width, compare_007.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    uv_unwrap.width, uv_unwrap.height = 140.0, 100.0
    cylinder.width, cylinder.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    join_geometry_003.width, join_geometry_003.height = 140.0, 100.0

    assemblymoduleblank.links.new(combine_xyz.outputs[0], cube.inputs[0])
    assemblymoduleblank.links.new(group_input.outputs[1], combine_xyz.inputs[0])
    assemblymoduleblank.links.new(group_input.outputs[1], combine_xyz.inputs[1])
    assemblymoduleblank.links.new(group_input.outputs[2], combine_xyz.inputs[2])
    assemblymoduleblank.links.new(cube.outputs[0], transform_geometry.inputs[0])
    assemblymoduleblank.links.new(
        combine_xyz_001.outputs[0], transform_geometry.inputs[1]
    )
    assemblymoduleblank.links.new(normal.outputs[0], compare_001.inputs[4])
    assemblymoduleblank.links.new(normal.outputs[0], separate_xyz.inputs[0])
    assemblymoduleblank.links.new(separate_xyz.outputs[0], compare_001.inputs[0])
    assemblymoduleblank.links.new(math_004.outputs[0], math_003.inputs[1])
    assemblymoduleblank.links.new(group_input_003.outputs[1], math_003.inputs[0])
    assemblymoduleblank.links.new(group_input_003.outputs[4], math_004.inputs[0])
    assemblymoduleblank.links.new(math_001.outputs[0], math_002.inputs[1])
    assemblymoduleblank.links.new(group_input_002.outputs[1], math_002.inputs[0])
    assemblymoduleblank.links.new(group_input_002.outputs[5], math_001.inputs[0])
    assemblymoduleblank.links.new(separate_xyz.outputs[1], compare.inputs[0])
    assemblymoduleblank.links.new(transform_geometry.outputs[0], set_position.inputs[0])
    assemblymoduleblank.links.new(math_003.outputs[0], combine_xyz_003.inputs[0])
    assemblymoduleblank.links.new(combine_xyz_003.outputs[0], set_position.inputs[3])
    assemblymoduleblank.links.new(compare_001.outputs[0], set_position.inputs[1])
    assemblymoduleblank.links.new(math_002.outputs[0], combine_xyz_002.inputs[1])
    assemblymoduleblank.links.new(
        combine_xyz_002.outputs[0], set_position_001.inputs[3]
    )
    assemblymoduleblank.links.new(set_position.outputs[0], set_position_001.inputs[0])
    assemblymoduleblank.links.new(compare.outputs[0], set_position_001.inputs[1])
    assemblymoduleblank.links.new(boolean_math.outputs[0], uv_unwrap.inputs[1])
    assemblymoduleblank.links.new(
        geometry_to_instance.outputs[0], instance_on_points.inputs[2]
    )
    assemblymoduleblank.links.new(instance_on_points.outputs[0], mesh_boolean.inputs[1])
    assemblymoduleblank.links.new(group_input_014.outputs[7], cylinder.inputs[0])
    assemblymoduleblank.links.new(math_014.outputs[0], math_013.inputs[1])
    assemblymoduleblank.links.new(group_input_009.outputs[1], math_013.inputs[0])
    assemblymoduleblank.links.new(group_input_009.outputs[8], math_014.inputs[0])
    assemblymoduleblank.links.new(math_013.outputs[0], combine_xyz_011.inputs[0])
    assemblymoduleblank.links.new(combine_xyz_011.outputs[0], points.inputs[1])
    assemblymoduleblank.links.new(points_002.outputs[0], join_geometry.inputs[0])
    assemblymoduleblank.links.new(
        join_geometry.outputs[0], transform_geometry_004.inputs[0]
    )
    assemblymoduleblank.links.new(
        group_input_006.outputs[6], instance_on_points.inputs[1]
    )
    assemblymoduleblank.links.new(
        combine_xyz_012.outputs[0], transform_geometry_004.inputs[1]
    )
    assemblymoduleblank.links.new(
        mesh_line_001.outputs[0], mesh_to_points_001.inputs[0]
    )
    assemblymoduleblank.links.new(
        mesh_to_points_001.outputs[0], instance_on_points_002.inputs[0]
    )
    assemblymoduleblank.links.new(
        transform_geometry_004.outputs[0], instance_on_points_002.inputs[2]
    )
    assemblymoduleblank.links.new(group_input_010.outputs[4], mesh_line_001.inputs[0])
    assemblymoduleblank.links.new(group_input_010.outputs[1], combine_xyz_013.inputs[0])
    assemblymoduleblank.links.new(combine_xyz_013.outputs[0], mesh_line_001.inputs[3])
    assemblymoduleblank.links.new(points_002.outputs[0], join_geometry_003.inputs[0])
    assemblymoduleblank.links.new(math_013.outputs[0], combine_xyz_010.inputs[1])
    assemblymoduleblank.links.new(combine_xyz_010.outputs[0], points_001.inputs[1])
    assemblymoduleblank.links.new(
        combine_xyz_012.outputs[0], transform_geometry_003.inputs[1]
    )
    assemblymoduleblank.links.new(
        join_geometry_003.outputs[0], transform_geometry_003.inputs[0]
    )
    assemblymoduleblank.links.new(
        transform_geometry_003.outputs[0], instance_on_points_001.inputs[0]
    )
    assemblymoduleblank.links.new(mesh_line.outputs[0], mesh_to_points.inputs[0])
    assemblymoduleblank.links.new(combine_xyz_014.outputs[0], mesh_line.inputs[3])
    assemblymoduleblank.links.new(
        mesh_to_points.outputs[0], instance_on_points_001.inputs[2]
    )
    assemblymoduleblank.links.new(
        merge_by_distance.outputs[0], instance_on_points.inputs[0]
    )
    assemblymoduleblank.links.new(
        instance_on_points_001.outputs[0], duplicate_elements_001.inputs[0]
    )
    assemblymoduleblank.links.new(
        duplicate_elements_001.outputs[0], transform_geometry_001.inputs[0]
    )
    assemblymoduleblank.links.new(
        combine_xyz_009.outputs[0], transform_geometry_001.inputs[1]
    )
    assemblymoduleblank.links.new(group_input_007.outputs[1], math_007.inputs[0])
    assemblymoduleblank.links.new(math_009.outputs[0], combine_xyz_009.inputs[0])
    assemblymoduleblank.links.new(math_007.outputs[0], math_009.inputs[0])
    assemblymoduleblank.links.new(group_input_007.outputs[8], math_008.inputs[0])
    assemblymoduleblank.links.new(math_008.outputs[0], math_009.inputs[1])
    assemblymoduleblank.links.new(group_input_007.outputs[4], math_007.inputs[1])
    assemblymoduleblank.links.new(
        duplicate_elements.outputs[0], transform_geometry_002.inputs[0]
    )
    assemblymoduleblank.links.new(
        combine_xyz_008.outputs[0], transform_geometry_002.inputs[1]
    )
    assemblymoduleblank.links.new(group_input_008.outputs[1], math_010.inputs[0])
    assemblymoduleblank.links.new(math_010.outputs[0], math_012.inputs[0])
    assemblymoduleblank.links.new(group_input_008.outputs[8], math_011.inputs[0])
    assemblymoduleblank.links.new(math_011.outputs[0], math_012.inputs[1])
    assemblymoduleblank.links.new(
        instance_on_points_002.outputs[0], duplicate_elements.inputs[0]
    )
    assemblymoduleblank.links.new(group_input_008.outputs[5], math_010.inputs[1])
    assemblymoduleblank.links.new(math_012.outputs[0], combine_xyz_008.inputs[1])
    assemblymoduleblank.links.new(
        realize_instances.outputs[0], merge_by_distance.inputs[0]
    )
    assemblymoduleblank.links.new(
        join_geometry_001.outputs[0], realize_instances.inputs[0]
    )
    assemblymoduleblank.links.new(group_input_014.outputs[9], math_020.inputs[0])
    assemblymoduleblank.links.new(math_020.outputs[0], cylinder.inputs[3])
    assemblymoduleblank.links.new(math.outputs[0], combine_xyz_001.inputs[0])
    assemblymoduleblank.links.new(math.outputs[0], combine_xyz_001.inputs[1])
    assemblymoduleblank.links.new(group_input_009.outputs[8], combine_xyz_012.inputs[0])
    assemblymoduleblank.links.new(group_input_009.outputs[8], combine_xyz_012.inputs[1])
    assemblymoduleblank.links.new(
        mesh_boolean.outputs[0], transform_geometry_005.inputs[0]
    )
    assemblymoduleblank.links.new(group_input_011.outputs[4], math_016.inputs[1])
    assemblymoduleblank.links.new(group_input_011.outputs[1], math_016.inputs[0])
    assemblymoduleblank.links.new(math_016.outputs[0], math_018.inputs[0])
    assemblymoduleblank.links.new(math_018.outputs[0], combine_xyz_015.inputs[0])
    assemblymoduleblank.links.new(math_015.outputs[0], math_017.inputs[0])
    assemblymoduleblank.links.new(group_input_011.outputs[5], math_015.inputs[1])
    assemblymoduleblank.links.new(group_input_011.outputs[1], math_015.inputs[0])
    assemblymoduleblank.links.new(math_017.outputs[0], combine_xyz_015.inputs[1])
    assemblymoduleblank.links.new(compare_002.outputs[0], set_position_003.inputs[1])
    assemblymoduleblank.links.new(group_input_004.outputs[3], math_005.inputs[0])
    assemblymoduleblank.links.new(
        combine_xyz_004.outputs[0], set_position_003.inputs[3]
    )
    assemblymoduleblank.links.new(compare_003.outputs[0], set_position_002.inputs[1])
    assemblymoduleblank.links.new(
        combine_xyz_005.outputs[0], set_position_002.inputs[3]
    )
    assemblymoduleblank.links.new(
        set_position_003.outputs[0], set_position_002.inputs[0]
    )
    assemblymoduleblank.links.new(separate_xyz_001.outputs[1], compare_003.inputs[0])
    assemblymoduleblank.links.new(separate_xyz_001.outputs[1], compare_002.inputs[0])
    assemblymoduleblank.links.new(group_input_004.outputs[3], combine_xyz_005.inputs[1])
    assemblymoduleblank.links.new(math_005.outputs[0], combine_xyz_004.inputs[1])
    assemblymoduleblank.links.new(set_position_002.outputs[0], mesh_boolean.inputs[0])
    assemblymoduleblank.links.new(group_input_014.outputs[2], cylinder.inputs[4])
    assemblymoduleblank.links.new(normal_001.outputs[0], separate_xyz_001.inputs[0])
    assemblymoduleblank.links.new(math_019.outputs[0], combine_xyz_016.inputs[2])
    assemblymoduleblank.links.new(
        vector_math_001.outputs[0], transform_geometry_005.inputs[1]
    )
    assemblymoduleblank.links.new(group_input_001.outputs[1], math.inputs[0])
    assemblymoduleblank.links.new(compare_005.outputs[0], set_position_004.inputs[1])
    assemblymoduleblank.links.new(group_input_005.outputs[3], math_006.inputs[0])
    assemblymoduleblank.links.new(
        combine_xyz_007.outputs[0], set_position_004.inputs[3]
    )
    assemblymoduleblank.links.new(compare_004.outputs[0], set_position_005.inputs[1])
    assemblymoduleblank.links.new(
        combine_xyz_006.outputs[0], set_position_005.inputs[3]
    )
    assemblymoduleblank.links.new(
        set_position_004.outputs[0], set_position_005.inputs[0]
    )
    assemblymoduleblank.links.new(
        set_position_005.outputs[0], set_position_003.inputs[0]
    )
    assemblymoduleblank.links.new(
        set_position_001.outputs[0], set_position_004.inputs[0]
    )
    assemblymoduleblank.links.new(math_006.outputs[0], combine_xyz_007.inputs[0])
    assemblymoduleblank.links.new(group_input_005.outputs[3], combine_xyz_006.inputs[0])
    assemblymoduleblank.links.new(separate_xyz_002.outputs[0], compare_005.inputs[0])
    assemblymoduleblank.links.new(separate_xyz_002.outputs[0], compare_004.inputs[0])
    assemblymoduleblank.links.new(normal_001.outputs[0], separate_xyz_002.inputs[0])
    assemblymoduleblank.links.new(group_input_010.outputs[1], combine_xyz_014.inputs[1])
    assemblymoduleblank.links.new(group_input_010.outputs[5], mesh_line.inputs[0])
    assemblymoduleblank.links.new(
        instance_on_points_001.outputs[0], join_geometry_002.inputs[0]
    )
    assemblymoduleblank.links.new(
        transform_geometry_002.outputs[0], join_geometry_001.inputs[0]
    )
    assemblymoduleblank.links.new(group_input_013.outputs[2], math_019.inputs[0])
    assemblymoduleblank.links.new(combine_xyz_015.outputs[0], vector_math.inputs[1])
    assemblymoduleblank.links.new(vector_math.outputs[0], vector_math_001.inputs[1])
    assemblymoduleblank.links.new(combine_xyz_016.outputs[0], vector_math_001.inputs[0])
    assemblymoduleblank.links.new(group_input_012.outputs[0], vector_math.inputs[0])
    assemblymoduleblank.links.new(
        store_named_attribute.outputs[0], geometry_to_instance.inputs[0]
    )
    assemblymoduleblank.links.new(
        set_shade_smooth.outputs[0], store_named_attribute.inputs[0]
    )
    assemblymoduleblank.links.new(
        compare_006.outputs[0], store_named_attribute.inputs[1]
    )
    assemblymoduleblank.links.new(separate_xyz_003.outputs[0], compare_006.inputs[0])
    assemblymoduleblank.links.new(normal_002.outputs[0], separate_xyz_003.inputs[0])
    assemblymoduleblank.links.new(uv_unwrap.outputs[0], group_output.inputs[1])
    assemblymoduleblank.links.new(
        transform_geometry_005.outputs[0], group_output.inputs[0]
    )
    assemblymoduleblank.links.new(named_attribute.outputs[3], boolean_math.inputs[1])
    assemblymoduleblank.links.new(edge_angle.outputs[0], compare_007.inputs[0])
    assemblymoduleblank.links.new(compare_007.outputs[0], boolean_math.inputs[0])
    assemblymoduleblank.links.new(cylinder.outputs[0], set_shade_smooth.inputs[0])
    assemblymoduleblank.links.new(cylinder.outputs[2], set_shade_smooth.inputs[1])
    assemblymoduleblank.links.new(points_001.outputs[0], join_geometry_003.inputs[0])
    assemblymoduleblank.links.new(points.outputs[0], join_geometry.inputs[0])
    assemblymoduleblank.links.new(
        instance_on_points_002.outputs[0], join_geometry_002.inputs[0]
    )
    assemblymoduleblank.links.new(
        join_geometry_002.outputs[0], join_geometry_001.inputs[0]
    )
    assemblymoduleblank.links.new(
        transform_geometry_001.outputs[0], join_geometry_001.inputs[0]
    )
    return assemblymoduleblank


assemblymoduleblank = assemblymoduleblank_node_group()
