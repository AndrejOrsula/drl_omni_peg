def assemblymodulehole_node_group():
    assemblymodulehole = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="AssemblyModuleHole"
    )

    frame_001 = assemblymodulehole.nodes.new("NodeFrame")
    frame_001.label = "Add wall around the hole into the original geometry"
    frame_001.use_custom_color = True
    frame_001.color = (0.1600000113248825, 0.17599999904632568, 0.20000000298023224)

    frame_002 = assemblymodulehole.nodes.new("NodeFrame")
    frame_002.label = "Get and process peg geometry to form the hole"
    frame_002.use_custom_color = True
    frame_002.color = (0.16862745583057404, 0.20000001788139343, 0.16078431904315948)

    frame_003 = assemblymodulehole.nodes.new("NodeFrame")
    frame_003.label = "Get peg geometry positioned and oriented above the hole"

    frame_004 = assemblymodulehole.nodes.new("NodeFrame")
    frame_004.label = "Translate peg geometry into the inserted pose"

    frame_005 = assemblymodulehole.nodes.new("NodeFrame")
    frame_005.label = "Extend the top of the peg"

    frame_006 = assemblymodulehole.nodes.new("NodeFrame")
    frame_006.label = "Hole: Add tolerance to the size of the peg"

    frame_007 = assemblymodulehole.nodes.new("NodeFrame")
    frame_007.label = "Get (random) origin and direction of the hole"

    frame_008 = assemblymodulehole.nodes.new("NodeFrame")
    frame_008.label = "Get peg geometry that is randomly rotated around its Z axis"

    frame_009 = assemblymodulehole.nodes.new("NodeFrame")
    frame_009.label = "(Experimental) Support pegs with holes in the middle"

    frame_010 = assemblymodulehole.nodes.new("NodeFrame")
    frame_010.label = "Remove inner holes from pegs"

    frame_011 = assemblymodulehole.nodes.new("NodeFrame")
    frame_011.label = "Walls: Add tolerance and wall width to the size of the peg"

    frame_012 = assemblymodulehole.nodes.new("NodeFrame")
    frame_012.label = "Add bottom portion to the wall geometry"

    frame_013 = assemblymodulehole.nodes.new("NodeFrame")
    frame_013.label = "Remove extra geometry from the walls above the hole"

    frame_014 = assemblymodulehole.nodes.new("NodeFrame")
    frame_014.label = "Merge original geometry with the walls"

    frame = assemblymodulehole.nodes.new("NodeFrame")
    frame.label = "Remove hole for the peg"

    reroute = assemblymodulehole.nodes.new("NodeReroute")
    reroute.label = "peg_pull_direction"
    reroute_001 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_001.label = "hole_position"
    reroute_002 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_003 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_003.label = "hole_position"
    reroute_006 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_007 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_007.label = "peg_insert_direction"
    reroute_008 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_008.label = "peg_pull_direction"
    assemblymodulehole.inputs.new("NodeSocketGeometry", "Geometry")
    assemblymodulehole.inputs[0].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketInt", "random_seed")
    assemblymodulehole.inputs[1].default_value = 0
    assemblymodulehole.inputs[1].min_value = 0
    assemblymodulehole.inputs[1].max_value = 2147483647
    assemblymodulehole.inputs[1].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketObject", "peg")
    assemblymodulehole.inputs[2].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketObject", "hole_position_handle")
    assemblymodulehole.inputs[3].attribute_domain = "POINT"

    assemblymodulehole.inputs.new(
        "NodeSocketVectorTranslation", "hole_position_offset_min"
    )
    assemblymodulehole.inputs[4].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.inputs[4].min_value = -3.4028234663852886e38
    assemblymodulehole.inputs[4].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[4].attribute_domain = "POINT"

    assemblymodulehole.inputs.new(
        "NodeSocketVectorTranslation", "hole_position_offset_max"
    )
    assemblymodulehole.inputs[5].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.inputs[5].min_value = -3.4028234663852886e38
    assemblymodulehole.inputs[5].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[5].attribute_domain = "POINT"

    assemblymodulehole.inputs.new(
        "NodeSocketVectorEuler", "hole_orientation_offset_min"
    )
    assemblymodulehole.inputs[6].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.inputs[6].min_value = -3.4028234663852886e38
    assemblymodulehole.inputs[6].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[6].attribute_domain = "POINT"

    assemblymodulehole.inputs.new(
        "NodeSocketVectorEuler", "hole_orientation_offset_max"
    )
    assemblymodulehole.inputs[7].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.inputs[7].min_value = -3.4028234663852886e38
    assemblymodulehole.inputs[7].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[7].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketFloatAngle", "hole_insertion_angle_min")
    assemblymodulehole.inputs[8].default_value = 0.0
    assemblymodulehole.inputs[8].min_value = -3.4028234663852886e38
    assemblymodulehole.inputs[8].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[8].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketFloatAngle", "hole_insertion_angle_max")
    assemblymodulehole.inputs[9].default_value = 0.0
    assemblymodulehole.inputs[9].min_value = -3.4028234663852886e38
    assemblymodulehole.inputs[9].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[9].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketFloatFactor", "hole_depth_factor_min")
    assemblymodulehole.inputs[10].default_value = 0.25
    assemblymodulehole.inputs[10].min_value = 0.0
    assemblymodulehole.inputs[10].max_value = 1.0
    assemblymodulehole.inputs[10].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketFloatFactor", "hole_depth_factor_max")
    assemblymodulehole.inputs[11].default_value = 0.75
    assemblymodulehole.inputs[11].min_value = 0.0
    assemblymodulehole.inputs[11].max_value = 1.0
    assemblymodulehole.inputs[11].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketFloatDistance", "hole_size_tolerance")
    assemblymodulehole.inputs[12].default_value = 0.0010000000474974513
    assemblymodulehole.inputs[12].min_value = 0.0
    assemblymodulehole.inputs[12].max_value = 3.4028234663852886e38
    assemblymodulehole.inputs[12].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketBool", "wall_enable")
    assemblymodulehole.inputs[13].default_value = True
    assemblymodulehole.inputs[13].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketBool", "wall_remove_inner_holes")
    assemblymodulehole.inputs[14].default_value = False
    assemblymodulehole.inputs[14].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketFloatDistance", "wall_thickness")
    assemblymodulehole.inputs[15].default_value = 0.005000000353902578
    assemblymodulehole.inputs[15].min_value = 9.999999747378752e-05
    assemblymodulehole.inputs[15].max_value = 10000.0
    assemblymodulehole.inputs[15].attribute_domain = "POINT"

    assemblymodulehole.inputs.new("NodeSocketBool", "wall_include_bottom")
    assemblymodulehole.inputs[16].default_value = True
    assemblymodulehole.inputs[16].attribute_domain = "POINT"

    group_input_001 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[1].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True
    group_input_001.outputs[11].hide = True
    group_input_001.outputs[12].hide = True
    group_input_001.outputs[13].hide = True
    group_input_001.outputs[14].hide = True
    group_input_001.outputs[15].hide = True
    group_input_001.outputs[16].hide = True
    group_input_001.outputs[17].hide = True

    position = assemblymodulehole.nodes.new("GeometryNodeInputPosition")

    object_info = assemblymodulehole.nodes.new("GeometryNodeObjectInfo")
    object_info.transform_space = "ORIGINAL"
    object_info.inputs[1].hide = True
    object_info.outputs[0].hide = True
    object_info.outputs[1].hide = True
    object_info.outputs[2].hide = True
    object_info.inputs[1].default_value = False

    attribute_statistic = assemblymodulehole.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.data_type = "FLOAT_VECTOR"
    attribute_statistic.domain = "POINT"
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.inputs[2].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[3].hide = True
    attribute_statistic.outputs[4].hide = True
    attribute_statistic.outputs[5].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    attribute_statistic.outputs[8].hide = True
    attribute_statistic.outputs[9].hide = True
    attribute_statistic.outputs[10].hide = True
    attribute_statistic.outputs[12].hide = True
    attribute_statistic.outputs[14].hide = True
    attribute_statistic.outputs[15].hide = True
    attribute_statistic.inputs[1].default_value = True
    attribute_statistic.inputs[2].default_value = 0.0

    vector_math = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math.operation = "MULTIPLY"
    vector_math.inputs[1].default_value = (0.0, 0.0, -1.0)
    vector_math.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math.inputs[3].default_value = 1.0

    align_euler_to_vector = assemblymodulehole.nodes.new(
        "FunctionNodeAlignEulerToVector"
    )
    align_euler_to_vector.axis = "Z"
    align_euler_to_vector.pivot_axis = "AUTO"
    align_euler_to_vector.inputs[0].hide = True
    align_euler_to_vector.inputs[1].hide = True
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    align_euler_to_vector.inputs[1].default_value = 1.0

    reroute_009 = assemblymodulehole.nodes.new("NodeReroute")
    separate_xyz = assemblymodulehole.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.outputs[0].hide = True
    separate_xyz.outputs[1].hide = True

    vector_rotate = assemblymodulehole.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.rotation_type = "EULER_XYZ"
    vector_rotate.inputs[1].hide = True
    vector_rotate.inputs[2].hide = True
    vector_rotate.inputs[3].hide = True
    vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_rotate.inputs[2].default_value = (0.0, 0.0, 1.0)
    vector_rotate.inputs[3].default_value = 0.0

    vector_math_001 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_001.operation = "ADD"
    vector_math_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_001.inputs[3].default_value = 1.0

    reroute_010 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_010.label = "peg_height"
    transform_geometry = assemblymodulehole.nodes.new("GeometryNodeTransform")
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    group_input_002 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    group_input_002.outputs[11].hide = True
    group_input_002.outputs[12].hide = True
    group_input_002.outputs[13].hide = True
    group_input_002.outputs[14].hide = True
    group_input_002.outputs[15].hide = True
    group_input_002.outputs[16].hide = True
    group_input_002.outputs[17].hide = True

    random_value = assemblymodulehole.nodes.new("FunctionNodeRandomValue")
    random_value.data_type = "FLOAT"
    random_value.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value.inputs[4].default_value = 3
    random_value.inputs[5].default_value = 10
    random_value.inputs[6].default_value = 0.5

    group_input_003 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[12].hide = True
    group_input_003.outputs[13].hide = True
    group_input_003.outputs[14].hide = True
    group_input_003.outputs[15].hide = True
    group_input_003.outputs[16].hide = True
    group_input_003.outputs[17].hide = True

    integer = assemblymodulehole.nodes.new("FunctionNodeInputInt")
    integer.integer = 3

    reroute_011 = assemblymodulehole.nodes.new("NodeReroute")
    math = assemblymodulehole.nodes.new("ShaderNodeMath")
    math.operation = "MULTIPLY"
    math.inputs[2].default_value = 0.5

    transform_geometry_001 = assemblymodulehole.nodes.new("GeometryNodeTransform")
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    capture_attribute = assemblymodulehole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.data_type = "FLOAT_VECTOR"
    capture_attribute.domain = "FACE"
    capture_attribute.inputs[2].default_value = 0.0
    capture_attribute.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    capture_attribute.inputs[4].default_value = False
    capture_attribute.inputs[5].default_value = 0

    normal = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    reroute_012 = assemblymodulehole.nodes.new("NodeReroute")
    vector_math_003 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_003.operation = "NORMALIZE"
    vector_math_003.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_003.inputs[3].default_value = 1.0

    vector_math_004 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_004.operation = "SCALE"
    vector_math_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_004.inputs[2].default_value = (0.0, 0.0, 0.0)

    vector_math_005 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_005.operation = "DOT_PRODUCT"
    vector_math_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_005.inputs[3].default_value = 1.0

    reroute_013 = assemblymodulehole.nodes.new("NodeReroute")
    normal_001 = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    math_001 = assemblymodulehole.nodes.new("ShaderNodeMath")
    math_001.operation = "MULTIPLY"
    math_001.inputs[1].default_value = 0.5
    math_001.inputs[2].default_value = 0.5

    vector_math_006 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_006.operation = "SUBTRACT"
    vector_math_006.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_006.inputs[3].default_value = 1.0

    group_input_004 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True
    group_input_004.outputs[15].hide = True
    group_input_004.outputs[16].hide = True
    group_input_004.outputs[17].hide = True

    vector_math_007 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_007.operation = "SCALE"
    vector_math_007.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_007.inputs[2].default_value = (0.0, 0.0, 0.0)

    capture_attribute_001 = assemblymodulehole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.data_type = "FLOAT_VECTOR"
    capture_attribute_001.domain = "FACE"
    capture_attribute_001.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    capture_attribute_001.inputs[4].default_value = False
    capture_attribute_001.inputs[5].default_value = 0

    vector_rotate_001 = assemblymodulehole.nodes.new("ShaderNodeVectorRotate")
    vector_rotate_001.rotation_type = "EULER_XYZ"
    vector_rotate_001.inputs[2].default_value = (0.0, 0.0, 1.0)
    vector_rotate_001.inputs[3].default_value = 0.0

    vector_math_008 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_008.operation = "ADD"
    vector_math_008.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_008.inputs[3].default_value = 1.0

    vector_math_009 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_009.operation = "ADD"
    vector_math_009.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_009.inputs[3].default_value = 1.0

    reroute_014 = assemblymodulehole.nodes.new("NodeReroute")
    group_input_005 = assemblymodulehole.nodes.new("NodeGroupInput")
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
    group_input_005.outputs[11].hide = True
    group_input_005.outputs[12].hide = True
    group_input_005.outputs[13].hide = True
    group_input_005.outputs[14].hide = True
    group_input_005.outputs[15].hide = True
    group_input_005.outputs[16].hide = True
    group_input_005.outputs[17].hide = True

    object_info_001 = assemblymodulehole.nodes.new("GeometryNodeObjectInfo")
    object_info_001.transform_space = "RELATIVE"
    object_info_001.inputs[1].hide = True
    object_info_001.outputs[2].hide = True
    object_info_001.outputs[3].hide = True
    object_info_001.inputs[1].default_value = False

    vector_math_010 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_010.operation = "MULTIPLY"
    vector_math_010.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_010.inputs[3].default_value = 1.0

    vector_math_011 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_011.operation = "MULTIPLY"
    vector_math_011.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_011.inputs[3].default_value = 1.0

    combine_xyz = assemblymodulehole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.inputs[0].hide = True
    combine_xyz.inputs[2].hide = True
    combine_xyz.inputs[0].default_value = 0.0
    combine_xyz.inputs[2].default_value = 0.0

    combine_xyz_001 = assemblymodulehole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.inputs[1].hide = True
    combine_xyz_001.inputs[2].hide = True
    combine_xyz_001.inputs[1].default_value = 0.0
    combine_xyz_001.inputs[2].default_value = 0.0

    separate_xyz_001 = assemblymodulehole.nodes.new("ShaderNodeSeparateXYZ")

    integer_001 = assemblymodulehole.nodes.new("FunctionNodeInputInt")

    group_input_006 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True
    group_input_006.outputs[15].hide = True
    group_input_006.outputs[16].hide = True
    group_input_006.outputs[17].hide = True

    group_input_007 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True
    group_input_007.outputs[11].hide = True
    group_input_007.outputs[12].hide = True
    group_input_007.outputs[13].hide = True
    group_input_007.outputs[14].hide = True
    group_input_007.outputs[15].hide = True
    group_input_007.outputs[16].hide = True
    group_input_007.outputs[17].hide = True

    random_value_001 = assemblymodulehole.nodes.new("FunctionNodeRandomValue")
    random_value_001.data_type = "FLOAT_VECTOR"
    random_value_001.inputs[2].default_value = 0.0
    random_value_001.inputs[3].default_value = 1.0
    random_value_001.inputs[4].default_value = 3
    random_value_001.inputs[5].default_value = 10
    random_value_001.inputs[6].default_value = 0.5

    def _get_parallel_vectors_node_group():
        _get_parallel_vectors = bpy.data.node_groups.new(
            type="GeometryNodeTree", name="_get_parallel_vectors"
        )

        _get_parallel_vectors.inputs.new("NodeSocketVectorXYZ", "input_z")
        _get_parallel_vectors.inputs[0].default_value = (0.0, 0.0, 0.0)
        _get_parallel_vectors.inputs[0].min_value = -10000.0
        _get_parallel_vectors.inputs[0].max_value = 10000.0
        _get_parallel_vectors.inputs[0].attribute_domain = "POINT"

        group_input = _get_parallel_vectors.nodes.new("NodeGroupInput")
        group_input.outputs[1].hide = True

        math_1 = _get_parallel_vectors.nodes.new("ShaderNodeMath")
        math_1.operation = "DIVIDE"
        math_1.inputs[2].default_value = 0.5

        combine_xyz_1 = _get_parallel_vectors.nodes.new("ShaderNodeCombineXYZ")
        combine_xyz_1.inputs[0].default_value = 1.0
        combine_xyz_1.inputs[1].default_value = 0.0

        separate_xyz_1 = _get_parallel_vectors.nodes.new("ShaderNodeSeparateXYZ")
        separate_xyz_1.outputs[1].hide = True

        vector_math_1 = _get_parallel_vectors.nodes.new("ShaderNodeVectorMath")
        vector_math_1.operation = "NORMALIZE"
        vector_math_1.inputs[1].default_value = (0.0, 0.0, 0.0)
        vector_math_1.inputs[2].default_value = (0.0, 0.0, 0.0)
        vector_math_1.inputs[3].default_value = 1.0

        vector_math_001_1 = _get_parallel_vectors.nodes.new("ShaderNodeVectorMath")
        vector_math_001_1.operation = "CROSS_PRODUCT"
        vector_math_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
        vector_math_001_1.inputs[3].default_value = 1.0

        math_001_1 = _get_parallel_vectors.nodes.new("ShaderNodeMath")
        math_001_1.operation = "MULTIPLY"
        math_001_1.inputs[1].default_value = -1.0
        math_001_1.inputs[2].default_value = 0.5

        _get_parallel_vectors.outputs.new("NodeSocketVectorXYZ", "output_x")
        _get_parallel_vectors.outputs[0].default_value = (0.0, 0.0, 0.0)
        _get_parallel_vectors.outputs[0].min_value = -3.4028234663852886e38
        _get_parallel_vectors.outputs[0].max_value = 3.4028234663852886e38
        _get_parallel_vectors.outputs[0].attribute_domain = "POINT"

        _get_parallel_vectors.outputs.new("NodeSocketVectorXYZ", "output_y")
        _get_parallel_vectors.outputs[1].default_value = (0.0, 0.0, 0.0)
        _get_parallel_vectors.outputs[1].min_value = -3.4028234663852886e38
        _get_parallel_vectors.outputs[1].max_value = 3.4028234663852886e38
        _get_parallel_vectors.outputs[1].attribute_domain = "POINT"

        group_output = _get_parallel_vectors.nodes.new("NodeGroupOutput")
        group_output.inputs[2].hide = True

        group_input.location = (-526.127197265625, -91.06910705566406)
        math_1.location = (43.872802734375, 50.398521423339844)
        combine_xyz_1.location = (233.872802734375, 32.898521423339844)
        separate_xyz_1.location = (-336.127197265625, 21.898521423339844)
        vector_math_1.location = (423.872802734375, 27.898521423339844)
        vector_math_001_1.location = (613.872802734375, -51.56910705566406)
        math_001_1.location = (-146.127197265625, 133.32717895507812)
        group_output.location = (803.872802734375, 10.398521423339844)

        group_input.width, group_input.height = 140.0, 100.0
        math_1.width, math_1.height = 140.0, 100.0
        combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
        separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
        vector_math_1.width, vector_math_1.height = 140.0, 100.0
        vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
        math_001_1.width, math_001_1.height = 140.0, 100.0
        group_output.width, group_output.height = 140.0, 100.0

        _get_parallel_vectors.links.new(math_001_1.outputs[0], math_1.inputs[0])
        _get_parallel_vectors.links.new(math_1.outputs[0], combine_xyz_1.inputs[2])
        _get_parallel_vectors.links.new(separate_xyz_1.outputs[0], math_001_1.inputs[0])
        _get_parallel_vectors.links.new(separate_xyz_1.outputs[2], math_1.inputs[1])
        _get_parallel_vectors.links.new(
            vector_math_1.outputs[0], group_output.inputs[0]
        )
        _get_parallel_vectors.links.new(
            vector_math_001_1.outputs[0], group_output.inputs[1]
        )
        _get_parallel_vectors.links.new(
            group_input.outputs[0], separate_xyz_1.inputs[0]
        )
        _get_parallel_vectors.links.new(
            group_input.outputs[0], vector_math_001_1.inputs[1]
        )
        _get_parallel_vectors.links.new(
            combine_xyz_1.outputs[0], vector_math_1.inputs[0]
        )
        _get_parallel_vectors.links.new(
            vector_math_1.outputs[0], vector_math_001_1.inputs[0]
        )
        return _get_parallel_vectors

    _get_parallel_vectors = _get_parallel_vectors_node_group()

    group = assemblymodulehole.nodes.new("GeometryNodeGroup")
    group.node_tree = bpy.data.node_groups["_get_parallel_vectors"]

    group_input_008 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[8].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    group_input_008.outputs[11].hide = True
    group_input_008.outputs[12].hide = True
    group_input_008.outputs[13].hide = True
    group_input_008.outputs[14].hide = True
    group_input_008.outputs[15].hide = True
    group_input_008.outputs[16].hide = True
    group_input_008.outputs[17].hide = True

    integer_002 = assemblymodulehole.nodes.new("FunctionNodeInputInt")
    integer_002.integer = 1

    group_input_009 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    group_input_009.outputs[11].hide = True
    group_input_009.outputs[12].hide = True
    group_input_009.outputs[13].hide = True
    group_input_009.outputs[14].hide = True
    group_input_009.outputs[15].hide = True
    group_input_009.outputs[16].hide = True
    group_input_009.outputs[17].hide = True

    random_value_002 = assemblymodulehole.nodes.new("FunctionNodeRandomValue")
    random_value_002.data_type = "FLOAT_VECTOR"
    random_value_002.inputs[2].default_value = 0.0
    random_value_002.inputs[3].default_value = 1.0
    random_value_002.inputs[4].default_value = 3
    random_value_002.inputs[5].default_value = 10
    random_value_002.inputs[6].default_value = 0.5

    normal_002 = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    group_input_010 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_010.outputs[1].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[4].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True
    group_input_010.outputs[11].hide = True
    group_input_010.outputs[12].hide = True
    group_input_010.outputs[13].hide = True
    group_input_010.outputs[14].hide = True
    group_input_010.outputs[15].hide = True
    group_input_010.outputs[16].hide = True
    group_input_010.outputs[17].hide = True

    sample_nearest_surface = assemblymodulehole.nodes.new(
        "GeometryNodeSampleNearestSurface"
    )
    sample_nearest_surface.data_type = "FLOAT_VECTOR"
    sample_nearest_surface.inputs[1].default_value = 0.0
    sample_nearest_surface.inputs[2].default_value = 0
    sample_nearest_surface.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
    sample_nearest_surface.inputs[5].default_value = False

    vector_math_012 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_012.operation = "ADD"
    vector_math_012.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_012.inputs[3].default_value = 1.0

    reroute_015 = assemblymodulehole.nodes.new("NodeReroute")
    group_input_011 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[4].hide = True
    group_input_011.outputs[5].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True
    group_input_011.outputs[15].hide = True
    group_input_011.outputs[16].hide = True
    group_input_011.outputs[17].hide = True

    group_input_012 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[10].hide = True
    group_input_012.outputs[11].hide = True
    group_input_012.outputs[12].hide = True
    group_input_012.outputs[13].hide = True
    group_input_012.outputs[14].hide = True
    group_input_012.outputs[15].hide = True
    group_input_012.outputs[16].hide = True
    group_input_012.outputs[17].hide = True

    integer_003 = assemblymodulehole.nodes.new("FunctionNodeInputInt")
    integer_003.integer = 2

    random_value_003 = assemblymodulehole.nodes.new("FunctionNodeRandomValue")
    random_value_003.data_type = "FLOAT"
    random_value_003.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value_003.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value_003.inputs[4].default_value = 3
    random_value_003.inputs[5].default_value = 10
    random_value_003.inputs[6].default_value = 0.5

    combine_xyz_002 = assemblymodulehole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[1].hide = True
    combine_xyz_002.inputs[0].default_value = 0.0
    combine_xyz_002.inputs[1].default_value = 0.0

    normal_003 = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    capture_attribute_002 = assemblymodulehole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_002.data_type = "FLOAT_VECTOR"
    capture_attribute_002.domain = "FACE"
    capture_attribute_002.inputs[2].default_value = 0.0
    capture_attribute_002.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    capture_attribute_002.inputs[4].default_value = False
    capture_attribute_002.inputs[5].default_value = 0

    transform_geometry_002 = assemblymodulehole.nodes.new("GeometryNodeTransform")
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    group_input_013 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[2].hide = True
    group_input_013.outputs[3].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True
    group_input_013.outputs[11].hide = True
    group_input_013.outputs[12].hide = True
    group_input_013.outputs[13].hide = True
    group_input_013.outputs[15].hide = True
    group_input_013.outputs[16].hide = True
    group_input_013.outputs[17].hide = True

    vector_math_013 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_013.operation = "SCALE"
    vector_math_013.inputs[1].default_value = (1.0, 1.0, 1.0)
    vector_math_013.inputs[2].default_value = (0.0, 0.0, 0.0)

    compare = assemblymodulehole.nodes.new("FunctionNodeCompare")
    compare.data_type = "VECTOR"
    compare.operation = "LESS_THAN"
    compare.mode = "DIRECTION"
    compare.inputs[0].default_value = 0.0
    compare.inputs[1].default_value = 0.0
    compare.inputs[2].default_value = 0
    compare.inputs[3].default_value = 0
    compare.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare.inputs[8].default_value = ""
    compare.inputs[9].default_value = ""
    compare.inputs[10].default_value = 0.8999999761581421
    compare.inputs[11].default_value = 1.5620696544647217
    compare.inputs[12].default_value = 0.10000000149011612

    transform_geometry_003 = assemblymodulehole.nodes.new("GeometryNodeTransform")
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    reroute_016 = assemblymodulehole.nodes.new("NodeReroute")
    vector_math_014 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_014.operation = "SCALE"
    vector_math_014.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_014.inputs[2].default_value = (0.0, 0.0, 0.0)

    vector_math_015 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_015.operation = "NORMALIZE"
    vector_math_015.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_015.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_015.inputs[3].default_value = 1.0

    vector_math_016 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_016.operation = "SUBTRACT"
    vector_math_016.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_016.inputs[3].default_value = 1.0

    vector_math_017 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_017.operation = "SCALE"
    vector_math_017.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_017.inputs[2].default_value = (0.0, 0.0, 0.0)

    vector_math_018 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_018.operation = "DOT_PRODUCT"
    vector_math_018.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_018.inputs[3].default_value = 1.0

    reroute_017 = assemblymodulehole.nodes.new("NodeReroute")
    capture_attribute_003 = assemblymodulehole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_003.data_type = "FLOAT_VECTOR"
    capture_attribute_003.domain = "FACE"
    capture_attribute_003.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    capture_attribute_003.inputs[4].default_value = False
    capture_attribute_003.inputs[5].default_value = 0

    normal_004 = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    math_002 = assemblymodulehole.nodes.new("ShaderNodeMath")
    math_002.operation = "ADD"
    math_002.inputs[2].default_value = 0.5

    group_input_014 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[2].hide = True
    group_input_014.outputs[3].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[7].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[9].hide = True
    group_input_014.outputs[10].hide = True
    group_input_014.outputs[11].hide = True
    group_input_014.outputs[12].hide = True
    group_input_014.outputs[13].hide = True
    group_input_014.outputs[14].hide = True
    group_input_014.outputs[16].hide = True
    group_input_014.outputs[17].hide = True

    compare_001 = assemblymodulehole.nodes.new("FunctionNodeCompare")
    compare_001.data_type = "VECTOR"
    compare_001.operation = "LESS_THAN"
    compare_001.mode = "DIRECTION"
    compare_001.inputs[0].default_value = 0.0
    compare_001.inputs[1].default_value = 0.0
    compare_001.inputs[2].default_value = 0
    compare_001.inputs[3].default_value = 0
    compare_001.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_001.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_001.inputs[8].default_value = ""
    compare_001.inputs[9].default_value = ""
    compare_001.inputs[10].default_value = 0.8999999761581421
    compare_001.inputs[11].default_value = 1.5620696544647217
    compare_001.inputs[12].default_value = 0.10000000149011612

    capture_attribute_004 = assemblymodulehole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_004.data_type = "FLOAT_VECTOR"
    capture_attribute_004.domain = "FACE"
    capture_attribute_004.inputs[2].default_value = 0.0
    capture_attribute_004.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    capture_attribute_004.inputs[4].default_value = False
    capture_attribute_004.inputs[5].default_value = 0

    normal_005 = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    group_input_015 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_015.outputs[0].hide = True
    group_input_015.outputs[1].hide = True
    group_input_015.outputs[2].hide = True
    group_input_015.outputs[3].hide = True
    group_input_015.outputs[4].hide = True
    group_input_015.outputs[5].hide = True
    group_input_015.outputs[6].hide = True
    group_input_015.outputs[7].hide = True
    group_input_015.outputs[8].hide = True
    group_input_015.outputs[9].hide = True
    group_input_015.outputs[10].hide = True
    group_input_015.outputs[11].hide = True
    group_input_015.outputs[12].hide = True
    group_input_015.outputs[13].hide = True
    group_input_015.outputs[14].hide = True
    group_input_015.outputs[15].hide = True
    group_input_015.outputs[17].hide = True

    capture_attribute_005 = assemblymodulehole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_005.data_type = "FLOAT_VECTOR"
    capture_attribute_005.domain = "FACE"
    capture_attribute_005.inputs[2].default_value = 0.0
    capture_attribute_005.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    capture_attribute_005.inputs[4].default_value = False
    capture_attribute_005.inputs[5].default_value = 0

    normal_006 = assemblymodulehole.nodes.new("GeometryNodeInputNormal")

    group_input_016 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_016.outputs[1].hide = True
    group_input_016.outputs[2].hide = True
    group_input_016.outputs[3].hide = True
    group_input_016.outputs[4].hide = True
    group_input_016.outputs[5].hide = True
    group_input_016.outputs[6].hide = True
    group_input_016.outputs[7].hide = True
    group_input_016.outputs[8].hide = True
    group_input_016.outputs[9].hide = True
    group_input_016.outputs[10].hide = True
    group_input_016.outputs[11].hide = True
    group_input_016.outputs[12].hide = True
    group_input_016.outputs[13].hide = True
    group_input_016.outputs[14].hide = True
    group_input_016.outputs[15].hide = True
    group_input_016.outputs[16].hide = True
    group_input_016.outputs[17].hide = True

    sample_nearest_surface_001 = assemblymodulehole.nodes.new(
        "GeometryNodeSampleNearestSurface"
    )
    sample_nearest_surface_001.data_type = "FLOAT_VECTOR"
    sample_nearest_surface_001.inputs[1].default_value = 0.0
    sample_nearest_surface_001.inputs[2].default_value = 0
    sample_nearest_surface_001.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
    sample_nearest_surface_001.inputs[5].default_value = False

    delete_geometry = assemblymodulehole.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.domain = "FACE"
    delete_geometry.mode = "ALL"

    compare_002 = assemblymodulehole.nodes.new("FunctionNodeCompare")
    compare_002.data_type = "VECTOR"
    compare_002.operation = "NOT_EQUAL"
    compare_002.mode = "DIRECTION"
    compare_002.inputs[0].default_value = 0.0
    compare_002.inputs[1].default_value = 0.0
    compare_002.inputs[2].default_value = 0
    compare_002.inputs[3].default_value = 0
    compare_002.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_002.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_002.inputs[8].default_value = ""
    compare_002.inputs[9].default_value = ""
    compare_002.inputs[10].default_value = 0.8999999761581421
    compare_002.inputs[11].default_value = 0.0
    compare_002.inputs[12].default_value = 0.10000000149011612

    mesh_boolean = assemblymodulehole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.operation = "DIFFERENCE"
    mesh_boolean.inputs[2].default_value = False
    mesh_boolean.inputs[3].default_value = False

    mesh_boolean_001 = assemblymodulehole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.operation = "UNION"
    mesh_boolean_001.inputs[2].default_value = False
    mesh_boolean_001.inputs[3].default_value = False

    group_input_017 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_017.outputs[1].hide = True
    group_input_017.outputs[2].hide = True
    group_input_017.outputs[3].hide = True
    group_input_017.outputs[4].hide = True
    group_input_017.outputs[5].hide = True
    group_input_017.outputs[6].hide = True
    group_input_017.outputs[7].hide = True
    group_input_017.outputs[8].hide = True
    group_input_017.outputs[9].hide = True
    group_input_017.outputs[10].hide = True
    group_input_017.outputs[11].hide = True
    group_input_017.outputs[12].hide = True
    group_input_017.outputs[13].hide = True
    group_input_017.outputs[14].hide = True
    group_input_017.outputs[15].hide = True
    group_input_017.outputs[16].hide = True
    group_input_017.outputs[17].hide = True

    transform_geometry_004 = assemblymodulehole.nodes.new("GeometryNodeTransform")
    transform_geometry_004.inputs[1].hide = True
    transform_geometry_004.inputs[3].hide = True
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    group_input_018 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_018.outputs[0].hide = True
    group_input_018.outputs[1].hide = True
    group_input_018.outputs[3].hide = True
    group_input_018.outputs[4].hide = True
    group_input_018.outputs[5].hide = True
    group_input_018.outputs[6].hide = True
    group_input_018.outputs[7].hide = True
    group_input_018.outputs[8].hide = True
    group_input_018.outputs[9].hide = True
    group_input_018.outputs[10].hide = True
    group_input_018.outputs[11].hide = True
    group_input_018.outputs[12].hide = True
    group_input_018.outputs[13].hide = True
    group_input_018.outputs[14].hide = True
    group_input_018.outputs[15].hide = True
    group_input_018.outputs[16].hide = True
    group_input_018.outputs[17].hide = True

    object_info_002 = assemblymodulehole.nodes.new("GeometryNodeObjectInfo")
    object_info_002.transform_space = "ORIGINAL"
    object_info_002.inputs[1].hide = True
    object_info_002.outputs[0].hide = True
    object_info_002.outputs[1].hide = True
    object_info_002.outputs[2].hide = True
    object_info_002.inputs[1].default_value = False

    convex_hull = assemblymodulehole.nodes.new("GeometryNodeConvexHull")

    compare_003 = assemblymodulehole.nodes.new("FunctionNodeCompare")
    compare_003.data_type = "VECTOR"
    compare_003.operation = "LESS_THAN"
    compare_003.mode = "DIRECTION"
    compare_003.inputs[0].default_value = 0.0
    compare_003.inputs[1].default_value = 0.0
    compare_003.inputs[2].default_value = 0
    compare_003.inputs[3].default_value = 0
    compare_003.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_003.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_003.inputs[8].default_value = ""
    compare_003.inputs[9].default_value = ""
    compare_003.inputs[10].default_value = 0.8999999761581421
    compare_003.inputs[11].default_value = 1.5620696544647217
    compare_003.inputs[12].default_value = 0.10000000149011612

    reroute_018 = assemblymodulehole.nodes.new("NodeReroute")
    attribute_statistic_001 = assemblymodulehole.nodes.new(
        "GeometryNodeAttributeStatistic"
    )
    attribute_statistic_001.data_type = "FLOAT"
    attribute_statistic_001.domain = "FACE"
    attribute_statistic_001.inputs[1].hide = True
    attribute_statistic_001.inputs[3].hide = True
    attribute_statistic_001.outputs[0].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[5].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True
    attribute_statistic_001.outputs[8].hide = True
    attribute_statistic_001.outputs[9].hide = True
    attribute_statistic_001.outputs[10].hide = True
    attribute_statistic_001.outputs[11].hide = True
    attribute_statistic_001.outputs[12].hide = True
    attribute_statistic_001.outputs[13].hide = True
    attribute_statistic_001.outputs[14].hide = True
    attribute_statistic_001.outputs[15].hide = True
    attribute_statistic_001.inputs[1].default_value = True
    attribute_statistic_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    object_info_003 = assemblymodulehole.nodes.new("GeometryNodeObjectInfo")
    object_info_003.transform_space = "ORIGINAL"
    object_info_003.inputs[1].hide = True
    object_info_003.outputs[0].hide = True
    object_info_003.outputs[1].hide = True
    object_info_003.outputs[2].hide = True
    object_info_003.inputs[1].default_value = False

    is_shade_smooth = assemblymodulehole.nodes.new("GeometryNodeInputShadeSmooth")

    group_input_019 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_019.outputs[0].hide = True
    group_input_019.outputs[1].hide = True
    group_input_019.outputs[3].hide = True
    group_input_019.outputs[4].hide = True
    group_input_019.outputs[5].hide = True
    group_input_019.outputs[6].hide = True
    group_input_019.outputs[7].hide = True
    group_input_019.outputs[8].hide = True
    group_input_019.outputs[9].hide = True
    group_input_019.outputs[10].hide = True
    group_input_019.outputs[11].hide = True
    group_input_019.outputs[12].hide = True
    group_input_019.outputs[13].hide = True
    group_input_019.outputs[14].hide = True
    group_input_019.outputs[15].hide = True
    group_input_019.outputs[16].hide = True
    group_input_019.outputs[17].hide = True

    compare_004 = assemblymodulehole.nodes.new("FunctionNodeCompare")
    compare_004.data_type = "VECTOR"
    compare_004.operation = "GREATER_THAN"
    compare_004.mode = "DIRECTION"
    compare_004.inputs[0].default_value = 0.0
    compare_004.inputs[1].default_value = 0.0
    compare_004.inputs[2].default_value = 0
    compare_004.inputs[3].default_value = 0
    compare_004.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_004.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
    compare_004.inputs[8].default_value = ""
    compare_004.inputs[9].default_value = ""
    compare_004.inputs[10].default_value = 0.8999999761581421
    compare_004.inputs[11].default_value = 1.579522967338562
    compare_004.inputs[12].default_value = 0.10000000149011612

    reroute_019 = assemblymodulehole.nodes.new("NodeReroute")
    group_input_020 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_020.outputs[0].hide = True
    group_input_020.outputs[1].hide = True
    group_input_020.outputs[2].hide = True
    group_input_020.outputs[3].hide = True
    group_input_020.outputs[4].hide = True
    group_input_020.outputs[5].hide = True
    group_input_020.outputs[6].hide = True
    group_input_020.outputs[7].hide = True
    group_input_020.outputs[8].hide = True
    group_input_020.outputs[9].hide = True
    group_input_020.outputs[10].hide = True
    group_input_020.outputs[11].hide = True
    group_input_020.outputs[12].hide = True
    group_input_020.outputs[13].hide = True
    group_input_020.outputs[14].hide = True
    group_input_020.outputs[16].hide = True
    group_input_020.outputs[17].hide = True

    vector_math_019 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_019.operation = "SCALE"
    vector_math_019.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_019.inputs[2].default_value = (0.0, 0.0, 0.0)

    def _decimate_planar_node_group():
        _decimate_planar = bpy.data.node_groups.new(
            type="GeometryNodeTree", name="_decimate_planar"
        )

        frame_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_1.label = "Transfer Normals"

        frame_001_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_001_1.label = "Create new Faces"

        frame_002_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_002_1.label = "Resample Curves"

        frame_003_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_003_1.label = "Instantiate new curves"

        frame_004_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_004_1.label = "Transfer original Positions"

        frame_005_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_005_1.label = "Remove Edges"

        frame_006_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_006_1.label = "Compare Directions to previous and next Point"

        frame_007_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_007_1.label = "Wrap Index  within a Spline"

        frame_008_1 = _decimate_planar.nodes.new("NodeFrame")
        frame_008_1.label = "Split Geometry at sharp Edges"

        join_geometry = _decimate_planar.nodes.new("GeometryNodeJoinGeometry")

        merge_by_distance = _decimate_planar.nodes.new("GeometryNodeMergeByDistance")
        merge_by_distance.mode = "ALL"
        merge_by_distance.inputs[1].default_value = True
        merge_by_distance.inputs[2].default_value = 0.0010000000474974513

        reroute_1 = _decimate_planar.nodes.new("NodeReroute")
        reroute_001_1 = _decimate_planar.nodes.new("NodeReroute")
        compare_1 = _decimate_planar.nodes.new("FunctionNodeCompare")
        compare_1.data_type = "VECTOR"
        compare_1.operation = "LESS_THAN"
        compare_1.mode = "DOT_PRODUCT"
        compare_1.inputs[0].default_value = 0.0
        compare_1.inputs[1].default_value = 0.0
        compare_1.inputs[2].default_value = 0
        compare_1.inputs[3].default_value = 0
        compare_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_1.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_1.inputs[8].default_value = ""
        compare_1.inputs[9].default_value = ""
        compare_1.inputs[10].default_value = 0.0
        compare_1.inputs[11].default_value = 0.08726649731397629
        compare_1.inputs[12].default_value = 0.0010000000474974513

        normal_1 = _decimate_planar.nodes.new("GeometryNodeInputNormal")

        position_1 = _decimate_planar.nodes.new("GeometryNodeInputPosition")

        normal_001_1 = _decimate_planar.nodes.new("GeometryNodeInputNormal")

        sample_nearest = _decimate_planar.nodes.new("GeometryNodeSampleNearest")
        sample_nearest.domain = "FACE"

        sample_index = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
        sample_index.data_type = "FLOAT_VECTOR"
        sample_index.domain = "FACE"
        sample_index.inputs[1].default_value = 0.0
        sample_index.inputs[2].default_value = 0
        sample_index.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
        sample_index.inputs[5].default_value = False

        _decimate_planar.outputs.new("NodeSocketGeometry", "Geometry")
        _decimate_planar.outputs[0].attribute_domain = "POINT"

        group_output_1 = _decimate_planar.nodes.new("NodeGroupOutput")

        reroute_002_1 = _decimate_planar.nodes.new("NodeReroute")
        mesh_line = _decimate_planar.nodes.new("GeometryNodeMeshLine")
        mesh_line.mode = "OFFSET"
        mesh_line.inputs[1].hide = True
        mesh_line.inputs[2].hide = True
        mesh_line.inputs[1].default_value = 1.0
        mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
        mesh_line.inputs[3].default_value = (1.0, 0.0, 0.0)

        domain_size = _decimate_planar.nodes.new("GeometryNodeAttributeDomainSize")
        domain_size.component = "CURVE"
        domain_size.outputs[0].hide = True
        domain_size.outputs[1].hide = True
        domain_size.outputs[2].hide = True
        domain_size.outputs[3].hide = True
        domain_size.outputs[5].hide = True

        sample_index_001 = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
        sample_index_001.data_type = "INT"
        sample_index_001.domain = "CURVE"
        sample_index_001.inputs[1].default_value = 0.0
        sample_index_001.inputs[3].default_value = (0.0, 0.0, 0.0)
        sample_index_001.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
        sample_index_001.inputs[5].default_value = False

        resample_curve = _decimate_planar.nodes.new("GeometryNodeResampleCurve")
        resample_curve.mode = "COUNT"
        resample_curve.inputs[1].default_value = True
        resample_curve.inputs[3].default_value = 0.10000000149011612

        index = _decimate_planar.nodes.new("GeometryNodeInputIndex")

        spline_length = _decimate_planar.nodes.new("GeometryNodeSplineLength")
        spline_length.outputs[0].hide = True

        fill_curve = _decimate_planar.nodes.new("GeometryNodeFillCurve")
        fill_curve.mode = "NGONS"

        sample_index_002 = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
        sample_index_002.data_type = "FLOAT_VECTOR"
        sample_index_002.domain = "POINT"
        sample_index_002.inputs[1].default_value = 0.0
        sample_index_002.inputs[2].default_value = 0
        sample_index_002.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
        sample_index_002.inputs[5].default_value = False

        position_001 = _decimate_planar.nodes.new("GeometryNodeInputPosition")

        index_001 = _decimate_planar.nodes.new("GeometryNodeInputIndex")

        set_position = _decimate_planar.nodes.new("GeometryNodeSetPosition")
        set_position.inputs[1].hide = True
        set_position.inputs[3].hide = True
        set_position.inputs[1].default_value = True
        set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

        realize_instances = _decimate_planar.nodes.new("GeometryNodeRealizeInstances")

        instance_on_points = _decimate_planar.nodes.new("GeometryNodeInstanceOnPoints")
        instance_on_points.inputs[1].hide = True
        instance_on_points.inputs[3].hide = True
        instance_on_points.inputs[4].hide = True
        instance_on_points.inputs[5].hide = True
        instance_on_points.inputs[6].hide = True
        instance_on_points.inputs[1].default_value = True
        instance_on_points.inputs[3].default_value = False
        instance_on_points.inputs[4].default_value = 0
        instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
        instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

        reroute_003_1 = _decimate_planar.nodes.new("NodeReroute")
        reroute_004 = _decimate_planar.nodes.new("NodeReroute")
        reroute_005 = _decimate_planar.nodes.new("NodeReroute")
        evaluate_at_index = _decimate_planar.nodes.new("GeometryNodeFieldAtIndex")
        evaluate_at_index.data_type = "FLOAT_VECTOR"
        evaluate_at_index.domain = "POINT"
        evaluate_at_index.inputs[1].default_value = 0.0
        evaluate_at_index.inputs[2].default_value = 0
        evaluate_at_index.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
        evaluate_at_index.inputs[5].default_value = False

        evaluate_at_index_001 = _decimate_planar.nodes.new("GeometryNodeFieldAtIndex")
        evaluate_at_index_001.data_type = "FLOAT_VECTOR"
        evaluate_at_index_001.domain = "POINT"
        evaluate_at_index_001.inputs[1].default_value = 0.0
        evaluate_at_index_001.inputs[2].default_value = 0
        evaluate_at_index_001.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
        evaluate_at_index_001.inputs[5].default_value = False

        edge_neighbors = _decimate_planar.nodes.new(
            "GeometryNodeInputMeshEdgeNeighbors"
        )

        compare_001_1 = _decimate_planar.nodes.new("FunctionNodeCompare")
        compare_001_1.data_type = "INT"
        compare_001_1.operation = "EQUAL"
        compare_001_1.mode = "ELEMENT"
        compare_001_1.inputs[0].default_value = 0.0
        compare_001_1.inputs[1].default_value = 0.0
        compare_001_1.inputs[3].default_value = 0
        compare_001_1.inputs[4].default_value = (0.0, 0.0, 0.0)
        compare_001_1.inputs[5].default_value = (0.0, 0.0, 0.0)
        compare_001_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_001_1.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_001_1.inputs[8].default_value = ""
        compare_001_1.inputs[9].default_value = ""
        compare_001_1.inputs[10].default_value = 0.8999999761581421
        compare_001_1.inputs[11].default_value = 0.08726649731397629
        compare_001_1.inputs[12].default_value = 0.0010000000474974513

        compare_002_1 = _decimate_planar.nodes.new("FunctionNodeCompare")
        compare_002_1.data_type = "INT"
        compare_002_1.operation = "GREATER_THAN"
        compare_002_1.mode = "ELEMENT"
        compare_002_1.inputs[0].default_value = 0.0
        compare_002_1.inputs[1].default_value = 0.0
        compare_002_1.inputs[3].default_value = 1
        compare_002_1.inputs[4].default_value = (0.0, 0.0, 0.0)
        compare_002_1.inputs[5].default_value = (0.0, 0.0, 0.0)
        compare_002_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_002_1.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_002_1.inputs[8].default_value = ""
        compare_002_1.inputs[9].default_value = ""
        compare_002_1.inputs[10].default_value = 0.8999999761581421
        compare_002_1.inputs[11].default_value = 0.08726649731397629
        compare_002_1.inputs[12].default_value = 0.0010000000474974513

        delete_geometry_1 = _decimate_planar.nodes.new("GeometryNodeDeleteGeometry")
        delete_geometry_1.domain = "EDGE"
        delete_geometry_1.mode = "EDGE_FACE"

        separate_geometry = _decimate_planar.nodes.new("GeometryNodeSeparateGeometry")
        separate_geometry.domain = "EDGE"

        reroute_006_1 = _decimate_planar.nodes.new("NodeReroute")
        spline_parameter = _decimate_planar.nodes.new("GeometryNodeSplineParameter")
        spline_parameter.outputs[0].hide = True
        spline_parameter.outputs[1].hide = True

        position_002 = _decimate_planar.nodes.new("GeometryNodeInputPosition")

        math_2 = _decimate_planar.nodes.new("ShaderNodeMath")
        math_2.operation = "SUBTRACT"
        math_2.inputs[1].default_value = 1.0
        math_2.inputs[2].default_value = 0.5

        spline_length_001 = _decimate_planar.nodes.new("GeometryNodeSplineLength")
        spline_length_001.outputs[0].hide = True

        math_001_2 = _decimate_planar.nodes.new("ShaderNodeMath")
        math_001_2.operation = "ADD"
        math_001_2.inputs[1].default_value = 1.0
        math_001_2.inputs[2].default_value = 0.5

        accumulate_field = _decimate_planar.nodes.new("GeometryNodeAccumulateField")
        accumulate_field.data_type = "INT"
        accumulate_field.domain = "CURVE"
        accumulate_field.inputs[0].hide = True
        accumulate_field.inputs[1].hide = True
        accumulate_field.inputs[3].hide = True
        accumulate_field.outputs[0].hide = True
        accumulate_field.outputs[1].hide = True
        accumulate_field.outputs[2].hide = True
        accumulate_field.outputs[3].hide = True
        accumulate_field.outputs[4].hide = True
        accumulate_field.outputs[6].hide = True
        accumulate_field.outputs[7].hide = True
        accumulate_field.outputs[8].hide = True
        accumulate_field.inputs[0].default_value = (1.0, 1.0, 1.0)
        accumulate_field.inputs[1].default_value = 1.0
        accumulate_field.inputs[3].default_value = 0

        math_002_1 = _decimate_planar.nodes.new("ShaderNodeMath")
        math_002_1.operation = "WRAP"
        math_002_1.inputs[2].default_value = 0.0

        math_003 = _decimate_planar.nodes.new("ShaderNodeMath")
        math_003.operation = "WRAP"
        math_003.inputs[2].default_value = 0.0

        curve_circle = _decimate_planar.nodes.new("GeometryNodeCurvePrimitiveCircle")
        curve_circle.mode = "RADIUS"
        curve_circle.inputs[0].default_value = 4
        curve_circle.inputs[1].default_value = (-1.0, 0.0, 0.0)
        curve_circle.inputs[2].default_value = (0.0, 1.0, 0.0)
        curve_circle.inputs[3].default_value = (1.0, 0.0, 0.0)
        curve_circle.inputs[4].default_value = 0.4000000059604645

        reroute_007_1 = _decimate_planar.nodes.new("NodeReroute")
        math_004 = _decimate_planar.nodes.new("ShaderNodeMath")
        math_004.operation = "ADD"
        math_004.inputs[2].default_value = 0.5

        mesh_to_curve = _decimate_planar.nodes.new("GeometryNodeMeshToCurve")
        mesh_to_curve.inputs[1].hide = True
        mesh_to_curve.inputs[1].default_value = True

        math_005 = _decimate_planar.nodes.new("ShaderNodeMath")
        math_005.operation = "ADD"
        math_005.inputs[2].default_value = 0.5

        position_003 = _decimate_planar.nodes.new("GeometryNodeInputPosition")

        vector_math_2 = _decimate_planar.nodes.new("ShaderNodeVectorMath")
        vector_math_2.operation = "SUBTRACT"
        vector_math_2.inputs[2].default_value = (0.0, 0.0, 0.0)
        vector_math_2.inputs[3].default_value = 1.0

        vector_math_001_2 = _decimate_planar.nodes.new("ShaderNodeVectorMath")
        vector_math_001_2.operation = "SUBTRACT"
        vector_math_001_2.inputs[2].default_value = (0.0, 0.0, 0.0)
        vector_math_001_2.inputs[3].default_value = 1.0

        compare_003_1 = _decimate_planar.nodes.new("FunctionNodeCompare")
        compare_003_1.data_type = "VECTOR"
        compare_003_1.operation = "EQUAL"
        compare_003_1.mode = "DIRECTION"
        compare_003_1.inputs[0].default_value = 0.0
        compare_003_1.inputs[1].default_value = 0.0
        compare_003_1.inputs[2].default_value = 0
        compare_003_1.inputs[3].default_value = 0
        compare_003_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_003_1.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_003_1.inputs[8].default_value = ""
        compare_003_1.inputs[9].default_value = ""
        compare_003_1.inputs[10].default_value = 1.0
        compare_003_1.inputs[11].default_value = 0.0
        compare_003_1.inputs[12].default_value = 0.0010000000474974513

        delete_geometry_001 = _decimate_planar.nodes.new("GeometryNodeDeleteGeometry")
        delete_geometry_001.domain = "POINT"
        delete_geometry_001.mode = "ALL"

        flip_faces = _decimate_planar.nodes.new("GeometryNodeFlipFaces")

        edge_angle = _decimate_planar.nodes.new("GeometryNodeInputMeshEdgeAngle")
        edge_angle.outputs[1].hide = True

        split_edges = _decimate_planar.nodes.new("GeometryNodeSplitEdges")

        _decimate_planar.inputs.new("NodeSocketGeometry", "Geometry")
        _decimate_planar.inputs[0].attribute_domain = "POINT"

        group_input_1 = _decimate_planar.nodes.new("NodeGroupInput")
        group_input_1.outputs[1].hide = True

        compare_004_1 = _decimate_planar.nodes.new("FunctionNodeCompare")
        compare_004_1.data_type = "FLOAT"
        compare_004_1.operation = "NOT_EQUAL"
        compare_004_1.mode = "ELEMENT"
        compare_004_1.inputs[1].default_value = 0.0
        compare_004_1.inputs[2].default_value = 0
        compare_004_1.inputs[3].default_value = 0
        compare_004_1.inputs[4].default_value = (0.0, 0.0, 0.0)
        compare_004_1.inputs[5].default_value = (0.0, 0.0, 0.0)
        compare_004_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_004_1.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
        compare_004_1.inputs[8].default_value = ""
        compare_004_1.inputs[9].default_value = ""
        compare_004_1.inputs[10].default_value = 0.8999999761581421
        compare_004_1.inputs[11].default_value = 0.08726649731397629
        compare_004_1.inputs[12].default_value = 0.0010000000474974513

        reroute_001_1.parent = frame_1
        compare_1.parent = frame_1
        normal_1.parent = frame_1
        position_1.parent = frame_1
        normal_001_1.parent = frame_1
        sample_nearest.parent = frame_1
        sample_index.parent = frame_1
        mesh_line.parent = frame_001_1
        domain_size.parent = frame_001_1
        sample_index_001.parent = frame_002_1
        resample_curve.parent = frame_002_1
        index.parent = frame_002_1
        spline_length.parent = frame_002_1
        fill_curve.parent = frame_002_1
        sample_index_002.parent = frame_004_1
        position_001.parent = frame_004_1
        index_001.parent = frame_004_1
        set_position.parent = frame_004_1
        realize_instances.parent = frame_003_1
        instance_on_points.parent = frame_003_1
        evaluate_at_index.parent = frame_006_1
        evaluate_at_index_001.parent = frame_006_1
        spline_parameter.parent = frame_007_1
        position_002.parent = frame_007_1
        math_2.parent = frame_007_1
        spline_length_001.parent = frame_007_1
        math_001_2.parent = frame_007_1
        accumulate_field.parent = frame_007_1
        math_002_1.parent = frame_007_1
        math_003.parent = frame_007_1
        curve_circle.parent = frame_003_1
        math_004.parent = frame_007_1
        math_005.parent = frame_007_1
        position_003.parent = frame_006_1
        vector_math_2.parent = frame_006_1
        vector_math_001_2.parent = frame_006_1
        compare_003_1.parent = frame_006_1
        delete_geometry_001.parent = frame_005_1
        edge_angle.parent = frame_008_1
        split_edges.parent = frame_008_1
        group_input_1.parent = frame_008_1
        compare_004_1.parent = frame_008_1

        frame_1.location = (0.0, 20.0)
        frame_001_1.location = (-210.0, -137.0)
        frame_002_1.location = (0.0, 0.0)
        frame_003_1.location = (0.0, 0.0)
        frame_004_1.location = (40.0, 40.0)
        frame_005_1.location = (-370.0, 3.0)
        frame_006_1.location = (-390.0, 23.0)
        frame_007_1.location = (-490.0, 23.0)
        frame_008_1.location = (-450.0, 23.0)
        join_geometry.location = (-100.0, 60.0)
        merge_by_distance.location = (80.0, 60.0)
        reroute_1.location = (-200.0, 40.0)
        reroute_001_1.location = (-660.0, 160.0)
        compare_1.location = (80.0, 300.0)
        normal_1.location = (-100.0, 300.0)
        position_1.location = (-700.0, 300.21575927734375)
        normal_001_1.location = (-520.0, 140.0)
        sample_nearest.location = (-520.0, 300.0)
        sample_index.location = (-300.0, 300.0)
        group_output_1.location = (580.0, 140.0)
        reroute_002_1.location = (-2560.0, 180.0)
        mesh_line.location = (-1230.0, -163.0)
        domain_size.location = (-1410.0, -163.0)
        sample_index_001.location = (-860.0, -20.0)
        resample_curve.location = (-680.0, -20.0)
        index.location = (-1040.0, -80.0)
        spline_length.location = (-1040.0, -20.0)
        fill_curve.location = (-500.0, -20.0)
        sample_index_002.location = (-500.0, -340.0)
        position_001.location = (-680.0, -340.0)
        index_001.location = (-680.0, -400.0)
        set_position.location = (-320.0, -340.0)
        realize_instances.location = (-860.0, -300.0)
        instance_on_points.location = (-1040.0, -300.0)
        reroute_003_1.location = (-1620.0, -580.0)
        reroute_004.location = (-760.0, -580.0)
        reroute_005.location = (-1720.0, -380.0)
        evaluate_at_index.location = (-2110.0, -583.0)
        evaluate_at_index_001.location = (-2110.0, -403.0)
        edge_neighbors.location = (-2860.0, -160.0)
        compare_001_1.location = (-2680.0, -200.0)
        compare_002_1.location = (-2680.0, -80.0)
        delete_geometry_1.location = (-2500.0, 60.0)
        separate_geometry.location = (-2320.0, 0.0)
        reroute_006_1.location = (-2100.0, 40.0)
        spline_parameter.location = (-2810.0, -603.0)
        position_002.location = (-2250.0, -603.0)
        math_2.location = (-2630.0, -483.0)
        spline_length_001.location = (-2630.0, -603.0)
        math_001_2.location = (-2630.0, -663.0)
        accumulate_field.location = (-2430.0, -543.0)
        math_002_1.location = (-2430.0, -403.0)
        math_003.location = (-2430.0, -703.0)
        curve_circle.location = (-1220.0, -380.0)
        reroute_007_1.location = (-1620.0, -160.0)
        math_004.location = (-2250.0, -483.0)
        mesh_to_curve.location = (-2140.0, -240.0)
        math_005.location = (-2250.0, -663.0)
        position_003.location = (-1930.0, -563.0)
        vector_math_2.location = (-1930.0, -443.0)
        vector_math_001_2.location = (-1930.0, -623.0)
        compare_003_1.location = (-1750.0, -463.0)
        delete_geometry_001.location = (-1550.0, -263.0)
        flip_faces.location = (300.0, 140.0)
        edge_angle.location = (-2990.0, -65.5)
        split_edges.location = (-2610.0, -43.0)
        group_input_1.location = (-2800.0, 35.0)
        compare_004_1.location = (-2800.0, -32.0)

        frame_1.width, frame_1.height = 980.0, 277.5
        frame_001_1.width, frame_001_1.height = 380.0, 254.5
        frame_002_1.width, frame_002_1.height = 740.0, 271.0
        frame_003_1.width, frame_003_1.height = 560.0, 279.0
        frame_004_1.width, frame_004_1.height = 560.0, 271.0
        frame_005_1.width, frame_005_1.height = 200.0, 219.5
        frame_006_1.width, frame_006_1.height = 560.0, 403.5
        frame_007_1.width, frame_007_1.height = 760.0, 486.5
        frame_008_1.width, frame_008_1.height = 580.0, 253.5
        join_geometry.width, join_geometry.height = 140.0, 100.0
        merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
        reroute_1.width, reroute_1.height = 100.0, 100.0
        reroute_001_1.width, reroute_001_1.height = 100.0, 100.0
        compare_1.width, compare_1.height = 140.0, 100.0
        normal_1.width, normal_1.height = 140.0, 100.0
        position_1.width, position_1.height = 140.0, 100.0
        normal_001_1.width, normal_001_1.height = 140.0, 100.0
        sample_nearest.width, sample_nearest.height = 140.0, 100.0
        sample_index.width, sample_index.height = 140.0, 100.0
        group_output_1.width, group_output_1.height = 140.0, 100.0
        reroute_002_1.width, reroute_002_1.height = 100.0, 100.0
        mesh_line.width, mesh_line.height = 140.0, 100.0
        domain_size.width, domain_size.height = 140.0, 100.0
        sample_index_001.width, sample_index_001.height = 140.0, 100.0
        resample_curve.width, resample_curve.height = 140.0, 100.0
        index.width, index.height = 140.0, 100.0
        spline_length.width, spline_length.height = 140.0, 100.0
        fill_curve.width, fill_curve.height = 140.0, 100.0
        sample_index_002.width, sample_index_002.height = 140.0, 100.0
        position_001.width, position_001.height = 140.0, 100.0
        index_001.width, index_001.height = 140.0, 100.0
        set_position.width, set_position.height = 140.0, 100.0
        realize_instances.width, realize_instances.height = 140.0, 100.0
        instance_on_points.width, instance_on_points.height = 140.0, 100.0
        reroute_003_1.width, reroute_003_1.height = 100.0, 100.0
        reroute_004.width, reroute_004.height = 100.0, 100.0
        reroute_005.width, reroute_005.height = 100.0, 100.0
        evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
        evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
        edge_neighbors.width, edge_neighbors.height = 140.0, 100.0
        compare_001_1.width, compare_001_1.height = 140.0, 100.0
        compare_002_1.width, compare_002_1.height = 140.0, 100.0
        delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
        separate_geometry.width, separate_geometry.height = 140.0, 100.0
        reroute_006_1.width, reroute_006_1.height = 100.0, 100.0
        spline_parameter.width, spline_parameter.height = 140.0, 100.0
        position_002.width, position_002.height = 140.0, 100.0
        math_2.width, math_2.height = 140.0, 100.0
        spline_length_001.width, spline_length_001.height = 140.0, 100.0
        math_001_2.width, math_001_2.height = 140.0, 100.0
        accumulate_field.width, accumulate_field.height = 140.0, 100.0
        math_002_1.width, math_002_1.height = 140.0, 100.0
        math_003.width, math_003.height = 140.0, 100.0
        curve_circle.width, curve_circle.height = 140.0, 100.0
        reroute_007_1.width, reroute_007_1.height = 100.0, 100.0
        math_004.width, math_004.height = 140.0, 100.0
        mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
        math_005.width, math_005.height = 140.0, 100.0
        position_003.width, position_003.height = 140.0, 100.0
        vector_math_2.width, vector_math_2.height = 140.0, 100.0
        vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
        compare_003_1.width, compare_003_1.height = 140.0, 100.0
        delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
        flip_faces.width, flip_faces.height = 140.0, 100.0
        edge_angle.width, edge_angle.height = 140.0, 100.0
        split_edges.width, split_edges.height = 140.0, 100.0
        group_input_1.width, group_input_1.height = 140.0, 100.0
        compare_004_1.width, compare_004_1.height = 140.0, 100.0

        _decimate_planar.links.new(flip_faces.outputs[0], group_output_1.inputs[0])
        _decimate_planar.links.new(edge_angle.outputs[0], compare_004_1.inputs[0])
        _decimate_planar.links.new(group_input_1.outputs[0], split_edges.inputs[0])
        _decimate_planar.links.new(compare_004_1.outputs[0], split_edges.inputs[1])
        _decimate_planar.links.new(split_edges.outputs[0], delete_geometry_1.inputs[0])
        _decimate_planar.links.new(edge_neighbors.outputs[0], compare_002_1.inputs[2])
        _decimate_planar.links.new(
            compare_002_1.outputs[0], delete_geometry_1.inputs[1]
        )
        _decimate_planar.links.new(edge_neighbors.outputs[0], compare_001_1.inputs[2])
        _decimate_planar.links.new(
            separate_geometry.outputs[0], mesh_to_curve.inputs[0]
        )
        _decimate_planar.links.new(
            delete_geometry_1.outputs[0], separate_geometry.inputs[0]
        )
        _decimate_planar.links.new(
            compare_001_1.outputs[0], separate_geometry.inputs[1]
        )
        _decimate_planar.links.new(spline_parameter.outputs[2], math_001_2.inputs[0])
        _decimate_planar.links.new(math_001_2.outputs[0], math_003.inputs[0])
        _decimate_planar.links.new(math_003.outputs[0], math_005.inputs[1])
        _decimate_planar.links.new(spline_length_001.outputs[1], math_003.inputs[1])
        _decimate_planar.links.new(
            spline_length_001.outputs[1], accumulate_field.inputs[2]
        )
        _decimate_planar.links.new(accumulate_field.outputs[5], math_005.inputs[0])
        _decimate_planar.links.new(position_002.outputs[0], evaluate_at_index.inputs[3])
        _decimate_planar.links.new(math_005.outputs[0], evaluate_at_index.inputs[0])
        _decimate_planar.links.new(spline_parameter.outputs[2], math_2.inputs[0])
        _decimate_planar.links.new(math_2.outputs[0], math_002_1.inputs[0])
        _decimate_planar.links.new(spline_length_001.outputs[1], math_002_1.inputs[1])
        _decimate_planar.links.new(math_002_1.outputs[0], math_004.inputs[0])
        _decimate_planar.links.new(accumulate_field.outputs[5], math_004.inputs[1])
        _decimate_planar.links.new(math_004.outputs[0], evaluate_at_index_001.inputs[0])
        _decimate_planar.links.new(
            position_002.outputs[0], evaluate_at_index_001.inputs[3]
        )
        _decimate_planar.links.new(position_003.outputs[0], vector_math_2.inputs[1])
        _decimate_planar.links.new(
            evaluate_at_index_001.outputs[2], vector_math_2.inputs[0]
        )
        _decimate_planar.links.new(vector_math_2.outputs[0], compare_003_1.inputs[4])
        _decimate_planar.links.new(
            vector_math_001_2.outputs[0], compare_003_1.inputs[5]
        )
        _decimate_planar.links.new(
            mesh_to_curve.outputs[0], delete_geometry_001.inputs[0]
        )
        _decimate_planar.links.new(
            compare_003_1.outputs[0], delete_geometry_001.inputs[1]
        )
        _decimate_planar.links.new(reroute_005.outputs[0], domain_size.inputs[0])
        _decimate_planar.links.new(position_001.outputs[0], sample_index_002.inputs[3])
        _decimate_planar.links.new(reroute_004.outputs[0], sample_index_002.inputs[0])
        _decimate_planar.links.new(sample_index_002.outputs[2], set_position.inputs[2])
        _decimate_planar.links.new(index_001.outputs[0], sample_index_002.inputs[6])
        _decimate_planar.links.new(set_position.outputs[0], join_geometry.inputs[0])
        _decimate_planar.links.new(
            join_geometry.outputs[0], merge_by_distance.inputs[0]
        )
        _decimate_planar.links.new(
            separate_geometry.outputs[1], reroute_006_1.inputs[0]
        )
        _decimate_planar.links.new(reroute_1.outputs[0], join_geometry.inputs[0])
        _decimate_planar.links.new(reroute_006_1.outputs[0], reroute_1.inputs[0])
        _decimate_planar.links.new(reroute_001_1.outputs[0], sample_index.inputs[0])
        _decimate_planar.links.new(position_1.outputs[0], sample_nearest.inputs[1])
        _decimate_planar.links.new(normal_001_1.outputs[0], sample_index.inputs[3])
        _decimate_planar.links.new(sample_nearest.outputs[0], sample_index.inputs[6])
        _decimate_planar.links.new(reroute_001_1.outputs[0], sample_nearest.inputs[0])
        _decimate_planar.links.new(merge_by_distance.outputs[0], flip_faces.inputs[0])
        _decimate_planar.links.new(compare_1.outputs[0], flip_faces.inputs[1])
        _decimate_planar.links.new(normal_1.outputs[0], compare_1.inputs[4])
        _decimate_planar.links.new(sample_index.outputs[2], compare_1.inputs[5])
        _decimate_planar.links.new(split_edges.outputs[0], reroute_002_1.inputs[0])
        _decimate_planar.links.new(reroute_002_1.outputs[0], reroute_001_1.inputs[0])
        _decimate_planar.links.new(
            curve_circle.outputs[0], instance_on_points.inputs[2]
        )
        _decimate_planar.links.new(mesh_line.outputs[0], instance_on_points.inputs[0])
        _decimate_planar.links.new(
            instance_on_points.outputs[0], realize_instances.inputs[0]
        )
        _decimate_planar.links.new(
            realize_instances.outputs[0], resample_curve.inputs[0]
        )
        _decimate_planar.links.new(reroute_007_1.outputs[0], sample_index_001.inputs[0])
        _decimate_planar.links.new(spline_length.outputs[1], sample_index_001.inputs[2])
        _decimate_planar.links.new(index.outputs[0], sample_index_001.inputs[6])
        _decimate_planar.links.new(
            sample_index_001.outputs[1], resample_curve.inputs[2]
        )
        _decimate_planar.links.new(fill_curve.outputs[0], set_position.inputs[0])
        _decimate_planar.links.new(resample_curve.outputs[0], fill_curve.inputs[0])
        _decimate_planar.links.new(domain_size.outputs[4], mesh_line.inputs[0])
        _decimate_planar.links.new(reroute_005.outputs[0], reroute_003_1.inputs[0])
        _decimate_planar.links.new(reroute_003_1.outputs[0], reroute_004.inputs[0])
        _decimate_planar.links.new(
            delete_geometry_001.outputs[0], reroute_005.inputs[0]
        )
        _decimate_planar.links.new(reroute_005.outputs[0], reroute_007_1.inputs[0])
        _decimate_planar.links.new(position_003.outputs[0], vector_math_001_2.inputs[0])
        _decimate_planar.links.new(
            evaluate_at_index.outputs[2], vector_math_001_2.inputs[1]
        )
        return _decimate_planar

    _decimate_planar = _decimate_planar_node_group()

    group_001 = assemblymodulehole.nodes.new("GeometryNodeGroup")
    group_001.node_tree = bpy.data.node_groups["_decimate_planar"]

    set_shade_smooth = assemblymodulehole.nodes.new("GeometryNodeSetShadeSmooth")

    boolean_math = assemblymodulehole.nodes.new("FunctionNodeBooleanMath")
    boolean_math.operation = "NOR"

    switch_001 = assemblymodulehole.nodes.new("GeometryNodeSwitch")
    switch_001.input_type = "GEOMETRY"
    switch_001.inputs[0].default_value = False
    switch_001.inputs[2].default_value = 0.0
    switch_001.inputs[3].default_value = 0.0
    switch_001.inputs[4].default_value = 0
    switch_001.inputs[5].default_value = 0
    switch_001.inputs[6].default_value = False
    switch_001.inputs[7].default_value = True
    switch_001.inputs[8].default_value = (0.0, 0.0, 0.0)
    switch_001.inputs[9].default_value = (0.0, 0.0, 0.0)
    switch_001.inputs[10].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    switch_001.inputs[11].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    switch_001.inputs[12].default_value = ""
    switch_001.inputs[13].default_value = ""

    set_position_001 = assemblymodulehole.nodes.new("GeometryNodeSetPosition")
    set_position_001.inputs[1].default_value = True
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    set_position_002 = assemblymodulehole.nodes.new("GeometryNodeSetPosition")
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    switch_002 = assemblymodulehole.nodes.new("GeometryNodeSwitch")
    switch_002.input_type = "GEOMETRY"
    switch_002.inputs[0].default_value = False
    switch_002.inputs[2].default_value = 0.0
    switch_002.inputs[3].default_value = 0.0
    switch_002.inputs[4].default_value = 0
    switch_002.inputs[5].default_value = 0
    switch_002.inputs[6].default_value = False
    switch_002.inputs[7].default_value = True
    switch_002.inputs[8].default_value = (0.0, 0.0, 0.0)
    switch_002.inputs[9].default_value = (0.0, 0.0, 0.0)
    switch_002.inputs[10].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    switch_002.inputs[11].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    switch_002.inputs[12].default_value = ""
    switch_002.inputs[13].default_value = ""

    reroute_020 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_020.label = "peg_insert_direction"
    vector_math_020 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_020.operation = "SCALE"
    vector_math_020.inputs[1].default_value = (1.0, 1.0, 1.0)
    vector_math_020.inputs[2].default_value = (0.0, 0.0, 0.0)

    group_input_021 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_021.outputs[1].hide = True
    group_input_021.outputs[2].hide = True
    group_input_021.outputs[3].hide = True
    group_input_021.outputs[4].hide = True
    group_input_021.outputs[5].hide = True
    group_input_021.outputs[6].hide = True
    group_input_021.outputs[7].hide = True
    group_input_021.outputs[8].hide = True
    group_input_021.outputs[9].hide = True
    group_input_021.outputs[10].hide = True
    group_input_021.outputs[11].hide = True
    group_input_021.outputs[12].hide = True
    group_input_021.outputs[13].hide = True
    group_input_021.outputs[14].hide = True
    group_input_021.outputs[15].hide = True
    group_input_021.outputs[16].hide = True
    group_input_021.outputs[17].hide = True

    position_001_1 = assemblymodulehole.nodes.new("GeometryNodeInputPosition")

    sample_nearest_surface_002 = assemblymodulehole.nodes.new(
        "GeometryNodeSampleNearestSurface"
    )
    sample_nearest_surface_002.data_type = "FLOAT_VECTOR"
    sample_nearest_surface_002.inputs[1].default_value = 0.0
    sample_nearest_surface_002.inputs[2].default_value = 0
    sample_nearest_surface_002.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
    sample_nearest_surface_002.inputs[5].default_value = False

    reroute_021 = assemblymodulehole.nodes.new("NodeReroute")
    vector_math_021 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_021.operation = "SCALE"
    vector_math_021.inputs[1].default_value = (-1.0, -1.0, -1.0)
    vector_math_021.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_021.inputs[3].default_value = -1.0

    reroute_022 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_022.label = "hole_position"
    reroute_023 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_023.label = "peg_pull_direction"
    reroute_024 = assemblymodulehole.nodes.new("NodeReroute")
    vector_math_002 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_002.operation = "SCALE"
    vector_math_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    reroute_005_1 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_005_1.label = "peg_insert_direction"
    reroute_026 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_027 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_004_1 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_004_1.label = "peg_with_tolerance"
    switch = assemblymodulehole.nodes.new("GeometryNodeSwitch")
    switch.input_type = "GEOMETRY"
    switch.inputs[0].default_value = False
    switch.inputs[2].default_value = 0.0
    switch.inputs[3].default_value = 0.0
    switch.inputs[4].default_value = 0
    switch.inputs[5].default_value = 0
    switch.inputs[6].default_value = False
    switch.inputs[7].default_value = True
    switch.inputs[8].default_value = (0.0, 0.0, 0.0)
    switch.inputs[9].default_value = (0.0, 0.0, 0.0)
    switch.inputs[10].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    switch.inputs[11].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    switch.inputs[12].default_value = ""
    switch.inputs[13].default_value = ""

    group_input_2 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_2.outputs[1].hide = True
    group_input_2.outputs[2].hide = True
    group_input_2.outputs[3].hide = True
    group_input_2.outputs[4].hide = True
    group_input_2.outputs[5].hide = True
    group_input_2.outputs[6].hide = True
    group_input_2.outputs[7].hide = True
    group_input_2.outputs[8].hide = True
    group_input_2.outputs[9].hide = True
    group_input_2.outputs[10].hide = True
    group_input_2.outputs[11].hide = True
    group_input_2.outputs[12].hide = True
    group_input_2.outputs[14].hide = True
    group_input_2.outputs[15].hide = True
    group_input_2.outputs[16].hide = True
    group_input_2.outputs[17].hide = True

    mesh_boolean_002 = assemblymodulehole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_002.operation = "DIFFERENCE"
    mesh_boolean_002.inputs[2].default_value = False
    mesh_boolean_002.inputs[3].default_value = False

    reroute_025 = assemblymodulehole.nodes.new("NodeReroute")
    reroute_028 = assemblymodulehole.nodes.new("NodeReroute")
    assemblymodulehole.outputs.new("NodeSocketGeometry", "Geometry")
    assemblymodulehole.outputs[0].attribute_domain = "POINT"

    assemblymodulehole.outputs.new("NodeSocketVectorXYZ", "entrance_position")
    assemblymodulehole.outputs[1].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.outputs[1].min_value = -3.4028234663852886e38
    assemblymodulehole.outputs[1].max_value = 3.4028234663852886e38
    assemblymodulehole.outputs[1].attribute_domain = "POINT"

    assemblymodulehole.outputs.new("NodeSocketVectorEuler", "entrance_orientation")
    assemblymodulehole.outputs[2].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.outputs[2].min_value = -3.4028234663852886e38
    assemblymodulehole.outputs[2].max_value = 3.4028234663852886e38
    assemblymodulehole.outputs[2].attribute_domain = "POINT"

    assemblymodulehole.outputs.new("NodeSocketVectorXYZ", "bottom_position")
    assemblymodulehole.outputs[3].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.outputs[3].min_value = -3.4028234663852886e38
    assemblymodulehole.outputs[3].max_value = 3.4028234663852886e38
    assemblymodulehole.outputs[3].attribute_domain = "POINT"

    assemblymodulehole.outputs.new("NodeSocketVectorEuler", "bottom_orientation")
    assemblymodulehole.outputs[4].default_value = (0.0, 0.0, 0.0)
    assemblymodulehole.outputs[4].min_value = -3.4028234663852886e38
    assemblymodulehole.outputs[4].max_value = 3.4028234663852886e38
    assemblymodulehole.outputs[4].attribute_domain = "POINT"

    group_output_2 = assemblymodulehole.nodes.new("NodeGroupOutput")

    raycast_001 = assemblymodulehole.nodes.new("GeometryNodeRaycast")
    raycast_001.data_type = "FLOAT"
    raycast_001.mapping = "INTERPOLATED"
    raycast_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    raycast_001.inputs[2].default_value = 0.0
    raycast_001.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    raycast_001.inputs[4].default_value = False
    raycast_001.inputs[5].default_value = 0
    raycast_001.inputs[8].default_value = 100.0

    align_euler_to_vector_001 = assemblymodulehole.nodes.new(
        "FunctionNodeAlignEulerToVector"
    )
    align_euler_to_vector_001.axis = "Z"
    align_euler_to_vector_001.pivot_axis = "AUTO"
    align_euler_to_vector_001.inputs[1].default_value = 1.0

    vector_math_022 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_022.operation = "ADD"
    vector_math_022.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_022.inputs[3].default_value = 1.0

    vector_math_023 = assemblymodulehole.nodes.new("ShaderNodeVectorMath")
    vector_math_023.operation = "SCALE"
    vector_math_023.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_023.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_023.inputs[3].default_value = -1.0

    group_input_022 = assemblymodulehole.nodes.new("NodeGroupInput")
    group_input_022.outputs[1].hide = True
    group_input_022.outputs[2].hide = True
    group_input_022.outputs[3].hide = True
    group_input_022.outputs[4].hide = True
    group_input_022.outputs[5].hide = True
    group_input_022.outputs[6].hide = True
    group_input_022.outputs[7].hide = True
    group_input_022.outputs[8].hide = True
    group_input_022.outputs[9].hide = True
    group_input_022.outputs[10].hide = True
    group_input_022.outputs[11].hide = True
    group_input_022.outputs[12].hide = True
    group_input_022.outputs[13].hide = True
    group_input_022.outputs[14].hide = True
    group_input_022.outputs[15].hide = True
    group_input_022.outputs[16].hide = True
    group_input_022.outputs[17].hide = True

    raycast = assemblymodulehole.nodes.new("GeometryNodeRaycast")
    raycast.data_type = "FLOAT"
    raycast.mapping = "INTERPOLATED"
    raycast.inputs[1].default_value = (0.0, 0.0, 0.0)
    raycast.inputs[2].default_value = 0.0
    raycast.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
    raycast.inputs[4].default_value = False
    raycast.inputs[5].default_value = 0
    raycast.inputs[8].default_value = 100.0

    extrude_mesh = assemblymodulehole.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.mode = "FACES"
    extrude_mesh.inputs[3].default_value = 1.0
    extrude_mesh.inputs[4].default_value = False

    set_position_1 = assemblymodulehole.nodes.new("GeometryNodeSetPosition")
    set_position_1.inputs[1].default_value = True
    set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    set_position_003 = assemblymodulehole.nodes.new("GeometryNodeSetPosition")
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    frame_003.parent = frame_002
    frame_004.parent = frame_002
    frame_005.parent = frame_002
    frame_006.parent = frame_002
    frame_009.parent = frame_001
    frame_010.parent = frame_009
    frame_011.parent = frame_001
    frame_012.parent = frame_001
    frame_013.parent = frame_001
    frame_014.parent = frame_001
    group_input_001.parent = frame_003
    position.parent = frame_003
    object_info.parent = frame_003
    attribute_statistic.parent = frame_003
    vector_math.parent = frame_003
    align_euler_to_vector.parent = frame_003
    reroute_009.parent = frame_003
    separate_xyz.parent = frame_003
    vector_rotate.parent = frame_003
    vector_math_001.parent = frame_003
    reroute_010.parent = frame_003
    transform_geometry.parent = frame_003
    group_input_002.parent = frame_004
    random_value.parent = frame_004
    group_input_003.parent = frame_004
    integer.parent = frame_004
    reroute_011.parent = frame_004
    math.parent = frame_004
    transform_geometry_001.parent = frame_004
    capture_attribute.parent = frame_005
    normal.parent = frame_005
    reroute_012.parent = frame_006
    vector_math_003.parent = frame_006
    vector_math_004.parent = frame_006
    vector_math_005.parent = frame_006
    reroute_013.parent = frame_006
    normal_001.parent = frame_006
    math_001.parent = frame_006
    vector_math_006.parent = frame_006
    group_input_004.parent = frame_006
    vector_math_007.parent = frame_006
    capture_attribute_001.parent = frame_006
    vector_rotate_001.parent = frame_007
    vector_math_008.parent = frame_007
    vector_math_009.parent = frame_007
    reroute_014.parent = frame_007
    group_input_005.parent = frame_007
    object_info_001.parent = frame_007
    vector_math_010.parent = frame_007
    vector_math_011.parent = frame_007
    combine_xyz.parent = frame_007
    combine_xyz_001.parent = frame_007
    separate_xyz_001.parent = frame_007
    integer_001.parent = frame_007
    group_input_006.parent = frame_007
    group_input_007.parent = frame_007
    random_value_001.parent = frame_007
    group.parent = frame_007
    group_input_008.parent = frame_007
    integer_002.parent = frame_007
    group_input_009.parent = frame_007
    random_value_002.parent = frame_007
    normal_002.parent = frame_007
    group_input_010.parent = frame_007
    sample_nearest_surface.parent = frame_007
    vector_math_012.parent = frame_007
    reroute_015.parent = frame_007
    group_input_011.parent = frame_008
    group_input_012.parent = frame_008
    integer_003.parent = frame_008
    random_value_003.parent = frame_008
    combine_xyz_002.parent = frame_008
    normal_003.parent = frame_009
    capture_attribute_002.parent = frame_009
    transform_geometry_002.parent = frame_009
    group_input_013.parent = frame_009
    vector_math_013.parent = frame_009
    compare.parent = frame_009
    transform_geometry_003.parent = frame_009
    reroute_016.parent = frame_011
    vector_math_014.parent = frame_011
    vector_math_015.parent = frame_011
    vector_math_016.parent = frame_011
    vector_math_017.parent = frame_011
    vector_math_018.parent = frame_011
    reroute_017.parent = frame_011
    capture_attribute_003.parent = frame_011
    normal_004.parent = frame_011
    math_002.parent = frame_011
    group_input_014.parent = frame_011
    compare_001.parent = frame_012
    capture_attribute_004.parent = frame_012
    normal_005.parent = frame_012
    group_input_015.parent = frame_012
    capture_attribute_005.parent = frame_013
    normal_006.parent = frame_013
    group_input_016.parent = frame_013
    sample_nearest_surface_001.parent = frame_013
    delete_geometry.parent = frame_013
    compare_002.parent = frame_013
    mesh_boolean.parent = frame_013
    mesh_boolean_001.parent = frame_014
    group_input_017.parent = frame_014
    transform_geometry_004.parent = frame_008
    group_input_018.parent = frame_008
    object_info_002.parent = frame_008
    convex_hull.parent = frame_010
    compare_003.parent = frame_005
    reroute_018.parent = frame_005
    attribute_statistic_001.parent = frame_005
    object_info_003.parent = frame_005
    is_shade_smooth.parent = frame_005
    group_input_019.parent = frame_005
    compare_004.parent = frame_005
    reroute_019.parent = frame_012
    group_input_020.parent = frame_012
    vector_math_019.parent = frame_012
    group_001.parent = frame_008
    set_shade_smooth.parent = frame_005
    boolean_math.parent = frame_005
    switch_001.parent = frame_009
    set_position_001.parent = frame_011
    set_position_002.parent = frame_012
    switch_002.parent = frame_012
    reroute_020.parent = frame_007
    vector_math_020.parent = frame_005
    group_input_021.parent = frame_007
    position_001_1.parent = frame_007
    sample_nearest_surface_002.parent = frame_007
    reroute_021.parent = frame_007
    vector_math_021.parent = frame_007
    reroute_022.parent = frame_007
    reroute_023.parent = frame_007
    vector_math_002.parent = frame_004
    reroute_027.parent = frame_008
    reroute_004_1.parent = frame
    switch.parent = frame
    group_input_2.parent = frame
    mesh_boolean_002.parent = frame
    extrude_mesh.parent = frame_009
    set_position_1.parent = frame_006
    set_position_003.parent = frame_005

    frame_001.location = (513.515625, 190.8028564453125)
    frame_002.location = (-4053.509765625, 844.9335327148438)
    frame_003.location = (-3648.28271484375, 198.9276123046875)
    frame_004.location = (-3128.17529296875, -757.0723876953125)
    frame_005.location = (-1750.1142578125, -651.0723876953125)
    frame_006.location = (1143.4736328125, -623.0723876953125)
    frame_007.location = (-9566.5546875, 252.6092529296875)
    frame_008.location = (-9641.5322265625, -783.0304565429688)
    frame_009.location = (-4700.29052734375, -8.06781005859375)
    frame_010.location = (-4567.50390625, -416.68975830078125)
    frame_011.location = (-4291.4853515625, 237.93218994140625)
    frame_012.location = (-2751.08984375, -868.0678100585938)
    frame_013.location = (-735.520263671875, -839.0678100585938)
    frame_014.location = (-1023.5537109375, -491.06781005859375)
    frame.location = (102.494140625, 473.3194885253906)
    reroute.location = (-9989.935546875, -888.8091430664062)
    reroute_001.location = (-9663.9150390625, -809.8853149414062)
    reroute_002.location = (-9130.2607421875, -1005.8109741210938)
    reroute_003.location = (-2314.447265625, -1005.8109741210938)
    reroute_006.location = (-5898.68798828125, -942.5845336914062)
    reroute_007.location = (-7860.53466796875, -935.8130493164062)
    reroute_008.location = (-7538.65966796875, -888.8091430664062)
    group_input_001.location = (-2699.43701171875, -610.5252685546875)
    position.location = (-2509.43701171875, -705.0252685546875)
    object_info.location = (-2509.43701171875, -583.0252685546875)
    attribute_statistic.location = (-2314.43701171875, -559.5252685546875)
    vector_math.location = (-2124.43701171875, -583.5276489257812)
    align_euler_to_vector.location = (-2124.43701171875, -825.7966918945312)
    reroute_009.location = (-2133.73974609375, -989.1820678710938)
    separate_xyz.location = (-1273.95556640625, -920.3519897460938)
    vector_rotate.location = (-1762.41796875, -616.0169677734375)
    vector_math_001.location = (-1472.26806640625, -626.5169677734375)
    reroute_010.location = (-710.29150390625, -959.3439331054688)
    transform_geometry.location = (-892.54248046875, -627.1513061523438)
    group_input_002.location = (-1077.099609375, 123.12406921386719)
    random_value.location = (-887.099609375, 298.0420837402344)
    group_input_003.location = (-1077.099609375, 307.12408447265625)
    integer.location = (-1077.099609375, 218.12408447265625)
    reroute_011.location = (-1047.9033203125, 345.3209533691406)
    math.location = (-697.099609375, 257.94915771484375)
    transform_geometry_001.location = (-317.099609375, 397.04498291015625)
    capture_attribute.location = (-1239.36474609375, 291.3905029296875)
    normal.location = (-1429.36474609375, 147.94754028320312)
    reroute_012.location = (-1523.92626953125, 212.9775390625)
    vector_math_003.location = (-1802.8603515625, 73.8314208984375)
    vector_math_004.location = (-1610.84423828125, 55.22772216796875)
    vector_math_005.location = (-2372.8603515625, 83.8314208984375)
    reroute_013.location = (-2747.20068359375, -112.7867431640625)
    normal_001.location = (-2750.84423828125, 101.25079345703125)
    math_001.location = (-1992.8603515625, -66.50848388671875)
    vector_math_006.location = (-1992.8603515625, 139.49151611328125)
    group_input_004.location = (-2182.8603515625, -153.15740966796875)
    vector_math_007.location = (-2182.8603515625, -9.15740966796875)
    capture_attribute_001.location = (-2560.84423828125, 262.5916748046875)
    vector_rotate_001.location = (-2391.31640625, -982.4521484375)
    vector_math_008.location = (-2678.8779296875, -1396.738037109375)
    vector_math_009.location = (-2911.892578125, -1043.40966796875)
    reroute_014.location = (-4063.1611328125, -1506.114501953125)
    group_input_005.location = (-4556.3837890625, -904.8895874023438)
    object_info_001.location = (-4366.3837890625, -876.3895874023438)
    vector_math_010.location = (-3101.892578125, -1043.40966796875)
    vector_math_011.location = (-3101.892578125, -1189.40966796875)
    combine_xyz.location = (-3451.7255859375, -1233.3857421875)
    combine_xyz_001.location = (-3451.7255859375, -1141.3857421875)
    separate_xyz_001.location = (-3641.7255859375, -1236.4434814453125)
    integer_001.location = (-4021.7255859375, -1278.84033203125)
    group_input_006.location = (-4021.7255859375, -1189.84033203125)
    group_input_007.location = (-4021.7255859375, -1373.84033203125)
    random_value_001.location = (-3831.7255859375, -1209.4434814453125)
    group.location = (-3451.7255859375, -938.2553100585938)
    group_input_008.location = (-4021.7255859375, -1714.110595703125)
    integer_002.location = (-4021.7255859375, -1619.110595703125)
    group_input_009.location = (-4021.7255859375, -1530.110595703125)
    random_value_002.location = (-3831.7255859375, -1552.233154296875)
    normal_002.location = (-4079.3896484375, -673.62548828125)
    group_input_010.location = (-4079.3896484375, -606.62548828125)
    sample_nearest_surface.location = (-3889.3896484375, -616.0238037109375)
    vector_math_012.location = (-2682.44921875, -790.1663818359375)
    reroute_015.location = (-2549.3232421875, -653.9478149414062)
    group_input_011.location = (-1077.099609375, 123.12406921386719)
    group_input_012.location = (-1077.099609375, 307.12408447265625)
    integer_003.location = (-1077.099609375, 218.12408447265625)
    random_value_003.location = (-887.099609375, 298.0420837402344)
    combine_xyz_002.location = (-697.099609375, 298.1568603515625)
    normal_003.location = (-3044.212890625, -527.2911376953125)
    capture_attribute_002.location = (-2854.212890625, -383.84814453125)
    transform_geometry_002.location = (-3310.3095703125, -420.71014404296875)
    group_input_013.location = (-1936.98779296875, -388.0589294433594)
    vector_math_013.location = (-2664.212890625, -698.5078735351562)
    compare.location = (-2664.212890625, -482.50787353515625)
    transform_geometry_003.location = (-4407.046875, -422.1256103515625)
    reroute_016.location = (-654.991943359375, -655.7918701171875)
    vector_math_014.location = (-741.909912109375, -793.4281005859375)
    vector_math_015.location = (-931.909912109375, -803.4281005859375)
    vector_math_016.location = (-1121.909912109375, -792.4281005859375)
    vector_math_017.location = (-1311.91015625, -886.4169311523438)
    vector_math_018.location = (-1501.909912109375, -793.4281005859375)
    reroute_017.location = (-1557.5458984375, -977.3161010742188)
    capture_attribute_003.location = (-1691.909912109375, -614.361572265625)
    normal_004.location = (-1881.91015625, -775.7024536132812)
    math_002.location = (-931.91015625, -939.255126953125)
    group_input_014.location = (-1121.91015625, -990.2550659179688)
    compare_001.location = (-1347.625, 142.58035278320312)
    capture_attribute_004.location = (-1613.553955078125, 249.26657104492188)
    normal_005.location = (-1803.553955078125, 99.11129760742188)
    group_input_015.location = (-477.7353515625, 440.43438720703125)
    capture_attribute_005.location = (-1847.3251953125, 209.8366241455078)
    normal_006.location = (-2042.3253173828125, -24.706893920898438)
    group_input_016.location = (-2042.3253173828125, 42.29313659667969)
    sample_nearest_surface_001.location = (-1852.3251953125, -20.496978759765625)
    delete_geometry.location = (-1462.3251953125, 290.1592712402344)
    compare_002.location = (-1652.3251953125, 107.35844421386719)
    mesh_boolean.location = (-1191.428466796875, 463.03387451171875)
    mesh_boolean_001.location = (-408.521240234375, 77.7578125)
    group_input_017.location = (-643.92822265625, 114.47882080078125)
    transform_geometry_004.location = (-317.099609375, 388.1473693847656)
    group_input_018.location = (-887.099609375, 378.1298828125)
    object_info_002.location = (-697.099609375, 431.916748046875)
    convex_hull.location = (-217.3515625, -140.37908935546875)
    compare_003.location = (-1049.36474609375, 192.73077392578125)
    reroute_018.location = (-1089.38330078125, 17.827835083007812)
    attribute_statistic_001.location = (-513.826171875, 27.43878173828125)
    object_info_003.location = (-705.20654296875, 31.53857421875)
    is_shade_smooth.location = (-705.20654296875, -90.46142578125)
    group_input_019.location = (-873.6982421875, -72.11468505859375)
    compare_004.location = (-1048.46484375, 459.92205810546875)
    reroute_019.location = (-1457.640625, -127.03033447265625)
    group_input_020.location = (-1309.314697265625, -110.83929443359375)
    vector_math_019.location = (-929.314697265625, 100.5137939453125)
    group_001.location = (-507.099609375, 420.97442626953125)
    set_shade_smooth.location = (-303.943359375, 283.190185546875)
    boolean_math.location = (-696.56982421875, 448.9088134765625)
    switch_001.location = (-1746.98779296875, -368.21966552734375)
    set_position_001.location = (-551.909912109375, -787.4281005859375)
    set_position_002.location = (-750.6748046875, 256.76806640625)
    switch_002.location = (-287.7352600097656, 491.57537841796875)
    reroute_020.location = (-1459.109375, -1188.42236328125)
    vector_math_020.location = (-1049.36474609375, -23.26922607421875)
    group_input_021.location = (-2046.375, -691.9337768554688)
    position_001_1.location = (-2046.375, -758.9338989257812)
    sample_nearest_surface_002.location = (-1853.875, -691.8521118164062)
    reroute_021.location = (-1932.453125, -1184.6629638671875)
    vector_math_021.location = (-1847.69140625, -1019.9051513671875)
    reroute_022.location = (-1459.109375, -1062.797119140625)
    reroute_023.location = (-1459.109375, -1141.41845703125)
    reroute_024.location = (-6506.2216796875, 1045.2396240234375)
    vector_math_002.location = (-507.099609375, 245.44915771484375)
    reroute_005_1.location = (-4217.4482421875, -957.7169799804688)
    reroute_026.location = (-599.883056640625, -1244.21435546875)
    reroute_027.location = (-446.9658203125, 283.25799560546875)
    reroute_004_1.location = (-609.2918701171875, -223.4200439453125)
    switch.location = (-462.2154541015625, -585.3873291015625)
    group_input_2.location = (-652.2154541015625, -624.8873291015625)
    mesh_boolean_002.location = (-87.98570251464844, -316.8748779296875)
    reroute_025.location = (37.5357666015625, 1073.1732177734375)
    reroute_028.location = (-512.5114135742188, -1055.477294921875)
    group_output_2.location = (1723.8592529296875, -87.35870361328125)
    raycast_001.location = (819.0977172851562, 492.8777770996094)
    align_euler_to_vector_001.location = (1047.785400390625, 194.20965576171875)
    vector_math_022.location = (795.4451904296875, -892.4864501953125)
    vector_math_023.location = (795.4451904296875, -739.8052368164062)
    group_input_022.location = (795.4451904296875, -656.651123046875)
    raycast.location = (1094.5030517578125, -500.71923828125)
    extrude_mesh.location = (-2232.50830078125, -384.2890625)
    set_position_1.location = (-1420.84423828125, 61.22772216796875)
    set_position_003.location = (-692.2578125, 253.62841796875)

    frame_001.width, frame_001.height = 8341.841796875, 793.2105102539062
    frame_002.width, frame_002.height = 6330.10498046875, 791.3158569335938
    frame_003.width, frame_003.height = 2056.3369140625, 506.76824951171875
    frame_004.width, frame_004.height = 960.42138671875, 395.65789794921875
    frame_005.width, frame_005.height = 1325.158203125, 681.76318359375
    frame_006.width, frame_006.height = 1534.0791015625, 551.9736938476562
    frame_007.width, frame_007.height = 3164.966796875, 1228.3946533203125
    frame_008.width, frame_008.height = 959.4736328125, 429.76318359375
    frame_009.width, frame_009.height = 3267.73681640625, 526.394775390625
    frame_010.width, frame_010.height = 199.68359375, 143.65789794921875
    frame_011.width, frame_011.height = 1529.78955078125, 546.2894287109375
    frame_012.width, frame_012.height = 1715.4736328125, 723.4473876953125
    frame_013.width, frame_013.height = 1050.4210205078125, 701.6578369140625
    frame_014.width, frame_014.height = 434.631591796875, 275.34210205078125
    frame.width, frame.height = 763.368408203125, 589.66259765625
    reroute.width, reroute.height = 16.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    reroute_003.width, reroute_003.height = 16.0, 100.0
    reroute_006.width, reroute_006.height = 16.0, 100.0
    reroute_007.width, reroute_007.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
    reroute_009.width, reroute_009.height = 16.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    vector_rotate.width, vector_rotate.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    reroute_010.width, reroute_010.height = 16.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    reroute_011.width, reroute_011.height = 16.0, 100.0
    math.width, math.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    reroute_012.width, reroute_012.height = 16.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    reroute_013.width, reroute_013.height = 16.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    vector_math_006.width, vector_math_006.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    vector_math_007.width, vector_math_007.height = 140.0, 100.0
    capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
    vector_rotate_001.width, vector_rotate_001.height = 140.0, 100.0
    vector_math_008.width, vector_math_008.height = 140.0, 100.0
    vector_math_009.width, vector_math_009.height = 140.0, 100.0
    reroute_014.width, reroute_014.height = 16.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    object_info_001.width, object_info_001.height = 140.0, 100.0
    vector_math_010.width, vector_math_010.height = 140.0, 100.0
    vector_math_011.width, vector_math_011.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    integer_002.width, integer_002.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 150.0, 100.0
    vector_math_012.width, vector_math_012.height = 140.0, 100.0
    reroute_015.width, reroute_015.height = 16.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    integer_003.width, integer_003.height = 140.0, 100.0
    random_value_003.width, random_value_003.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    normal_003.width, normal_003.height = 140.0, 100.0
    capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    vector_math_013.width, vector_math_013.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    reroute_016.width, reroute_016.height = 16.0, 100.0
    vector_math_014.width, vector_math_014.height = 140.0, 100.0
    vector_math_015.width, vector_math_015.height = 140.0, 100.0
    vector_math_016.width, vector_math_016.height = 140.0, 100.0
    vector_math_017.width, vector_math_017.height = 140.0, 100.0
    vector_math_018.width, vector_math_018.height = 140.0, 100.0
    reroute_017.width, reroute_017.height = 16.0, 100.0
    capture_attribute_003.width, capture_attribute_003.height = 140.0, 100.0
    normal_004.width, normal_004.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    capture_attribute_004.width, capture_attribute_004.height = 140.0, 100.0
    normal_005.width, normal_005.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    capture_attribute_005.width, capture_attribute_005.height = 140.0, 100.0
    normal_006.width, normal_006.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    sample_nearest_surface_001.width, sample_nearest_surface_001.height = 150.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    object_info_002.width, object_info_002.height = 140.0, 100.0
    convex_hull.width, convex_hull.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    reroute_018.width, reroute_018.height = 16.0, 100.0
    attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
    object_info_003.width, object_info_003.height = 140.0, 100.0
    is_shade_smooth.width, is_shade_smooth.height = 140.0, 100.0
    group_input_019.width, group_input_019.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    reroute_019.width, reroute_019.height = 16.0, 100.0
    group_input_020.width, group_input_020.height = 140.0, 100.0
    vector_math_019.width, vector_math_019.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    reroute_020.width, reroute_020.height = 16.0, 100.0
    vector_math_020.width, vector_math_020.height = 140.0, 100.0
    group_input_021.width, group_input_021.height = 140.0, 100.0
    position_001_1.width, position_001_1.height = 140.0, 100.0
    sample_nearest_surface_002.width, sample_nearest_surface_002.height = 150.0, 100.0
    reroute_021.width, reroute_021.height = 16.0, 100.0
    vector_math_021.width, vector_math_021.height = 140.0, 100.0
    reroute_022.width, reroute_022.height = 16.0, 100.0
    reroute_023.width, reroute_023.height = 16.0, 100.0
    reroute_024.width, reroute_024.height = 16.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
    reroute_026.width, reroute_026.height = 16.0, 100.0
    reroute_027.width, reroute_027.height = 16.0, 100.0
    reroute_004_1.width, reroute_004_1.height = 16.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    mesh_boolean_002.width, mesh_boolean_002.height = 140.0, 100.0
    reroute_025.width, reroute_025.height = 16.0, 100.0
    reroute_028.width, reroute_028.height = 16.0, 100.0
    group_output_2.width, group_output_2.height = 140.0, 100.0
    raycast_001.width, raycast_001.height = 150.0, 100.0
    align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
    vector_math_022.width, vector_math_022.height = 140.0, 100.0
    vector_math_023.width, vector_math_023.height = 140.0, 100.0
    group_input_022.width, group_input_022.height = 140.0, 100.0
    raycast.width, raycast.height = 150.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    set_position_1.width, set_position_1.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0

    assemblymodulehole.links.new(group_input_001.outputs[2], object_info.inputs[0])
    assemblymodulehole.links.new(object_info.outputs[3], attribute_statistic.inputs[0])
    assemblymodulehole.links.new(position.outputs[0], attribute_statistic.inputs[3])
    assemblymodulehole.links.new(
        position_001_1.outputs[0], sample_nearest_surface_002.inputs[3]
    )
    assemblymodulehole.links.new(
        object_info_001.outputs[0], sample_nearest_surface.inputs[6]
    )
    assemblymodulehole.links.new(
        normal_002.outputs[0], sample_nearest_surface.inputs[3]
    )
    assemblymodulehole.links.new(reroute.outputs[0], align_euler_to_vector.inputs[2])
    assemblymodulehole.links.new(
        group_input_021.outputs[0], sample_nearest_surface_002.inputs[0]
    )
    assemblymodulehole.links.new(
        align_euler_to_vector.outputs[0], transform_geometry.inputs[2]
    )
    assemblymodulehole.links.new(
        align_euler_to_vector.outputs[0], vector_rotate.inputs[4]
    )
    assemblymodulehole.links.new(vector_rotate.outputs[0], vector_math_001.inputs[0])
    assemblymodulehole.links.new(group_input_005.outputs[3], object_info_001.inputs[0])
    assemblymodulehole.links.new(vector_math.outputs[0], vector_rotate.inputs[0])
    assemblymodulehole.links.new(attribute_statistic.outputs[11], vector_math.inputs[0])
    assemblymodulehole.links.new(
        vector_math_001.outputs[0], transform_geometry.inputs[1]
    )
    assemblymodulehole.links.new(attribute_statistic.outputs[13], reroute_009.inputs[0])
    assemblymodulehole.links.new(
        reroute_011.outputs[0], transform_geometry_001.inputs[0]
    )
    assemblymodulehole.links.new(separate_xyz.outputs[2], reroute_010.inputs[0])
    assemblymodulehole.links.new(reroute_009.outputs[0], separate_xyz.inputs[0])
    assemblymodulehole.links.new(group_input_002.outputs[1], random_value.inputs[8])
    assemblymodulehole.links.new(integer.outputs[0], random_value.inputs[7])
    assemblymodulehole.links.new(group_input_003.outputs[10], random_value.inputs[2])
    assemblymodulehole.links.new(reroute_010.outputs[0], math.inputs[1])
    assemblymodulehole.links.new(random_value.outputs[1], math.inputs[0])
    assemblymodulehole.links.new(normal_005.outputs[0], capture_attribute_004.inputs[1])
    assemblymodulehole.links.new(group_input_015.outputs[16], switch_002.inputs[1])
    assemblymodulehole.links.new(mesh_boolean.outputs[0], mesh_boolean_001.inputs[1])
    assemblymodulehole.links.new(switch_002.outputs[6], mesh_boolean.inputs[0])
    assemblymodulehole.links.new(group_input_017.outputs[0], mesh_boolean_001.inputs[1])
    assemblymodulehole.links.new(reroute_006.outputs[0], reroute_005_1.inputs[0])
    assemblymodulehole.links.new(reroute_019.outputs[0], compare_001.inputs[5])
    assemblymodulehole.links.new(
        capture_attribute_004.outputs[1], compare_001.inputs[4]
    )
    assemblymodulehole.links.new(reroute_004_1.outputs[0], mesh_boolean_002.inputs[1])
    assemblymodulehole.links.new(reroute_002.outputs[0], reroute_003.inputs[0])
    assemblymodulehole.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
    assemblymodulehole.links.new(normal.outputs[0], capture_attribute.inputs[1])
    assemblymodulehole.links.new(capture_attribute.outputs[1], compare_003.inputs[4])
    assemblymodulehole.links.new(
        transform_geometry_001.outputs[0], capture_attribute.inputs[0]
    )
    assemblymodulehole.links.new(reroute_020.outputs[0], reroute_007.inputs[0])
    assemblymodulehole.links.new(transform_geometry.outputs[0], reroute_011.inputs[0])
    assemblymodulehole.links.new(reroute_005_1.outputs[0], reroute_019.inputs[0])
    assemblymodulehole.links.new(set_position_1.outputs[0], reroute_004_1.inputs[0])
    assemblymodulehole.links.new(group_input_007.outputs[1], random_value_001.inputs[8])
    assemblymodulehole.links.new(integer_001.outputs[0], random_value_001.inputs[7])
    assemblymodulehole.links.new(group_input_003.outputs[11], random_value.inputs[3])
    assemblymodulehole.links.new(group_input_006.outputs[5], random_value_001.inputs[1])
    assemblymodulehole.links.new(group_input_006.outputs[4], random_value_001.inputs[0])
    assemblymodulehole.links.new(object_info_001.outputs[0], vector_math_012.inputs[0])
    assemblymodulehole.links.new(sample_nearest_surface.outputs[2], group.inputs[0])
    assemblymodulehole.links.new(
        random_value_001.outputs[0], separate_xyz_001.inputs[0]
    )
    assemblymodulehole.links.new(separate_xyz_001.outputs[0], combine_xyz_001.inputs[0])
    assemblymodulehole.links.new(combine_xyz_001.outputs[0], vector_math_010.inputs[1])
    assemblymodulehole.links.new(group.outputs[0], vector_math_010.inputs[0])
    assemblymodulehole.links.new(vector_math_010.outputs[0], vector_math_009.inputs[0])
    assemblymodulehole.links.new(combine_xyz.outputs[0], vector_math_011.inputs[1])
    assemblymodulehole.links.new(separate_xyz_001.outputs[1], combine_xyz.inputs[1])
    assemblymodulehole.links.new(group.outputs[1], vector_math_011.inputs[0])
    assemblymodulehole.links.new(vector_math_011.outputs[0], vector_math_009.inputs[1])
    assemblymodulehole.links.new(vector_math_009.outputs[0], vector_math_012.inputs[1])
    assemblymodulehole.links.new(
        vector_math_012.outputs[0], sample_nearest_surface_002.inputs[6]
    )
    assemblymodulehole.links.new(group_input_008.outputs[1], random_value_002.inputs[8])
    assemblymodulehole.links.new(integer_002.outputs[0], random_value_002.inputs[7])
    assemblymodulehole.links.new(group_input_009.outputs[6], random_value_002.inputs[0])
    assemblymodulehole.links.new(group_input_009.outputs[7], random_value_002.inputs[1])
    assemblymodulehole.links.new(
        vector_math_012.outputs[0], vector_rotate_001.inputs[1]
    )
    assemblymodulehole.links.new(
        normal_006.outputs[0], sample_nearest_surface_001.inputs[3]
    )
    assemblymodulehole.links.new(
        vector_math_008.outputs[0], vector_rotate_001.inputs[4]
    )
    assemblymodulehole.links.new(reroute_014.outputs[0], vector_math_008.inputs[0])
    assemblymodulehole.links.new(random_value_002.outputs[0], vector_math_008.inputs[1])
    assemblymodulehole.links.new(object_info_001.outputs[1], reroute_014.inputs[0])
    assemblymodulehole.links.new(
        sample_nearest_surface.outputs[2], reroute_015.inputs[0]
    )
    assemblymodulehole.links.new(reroute_021.outputs[0], reroute_020.inputs[0])
    assemblymodulehole.links.new(vector_math_021.outputs[0], reroute_023.inputs[0])
    assemblymodulehole.links.new(
        sample_nearest_surface_002.outputs[2], reroute_022.inputs[0]
    )
    assemblymodulehole.links.new(
        group_input_010.outputs[0], sample_nearest_surface.inputs[0]
    )
    assemblymodulehole.links.new(vector_rotate_001.outputs[0], reroute_021.inputs[0])
    assemblymodulehole.links.new(reroute_023.outputs[0], reroute.inputs[0])
    assemblymodulehole.links.new(reroute_022.outputs[0], reroute_001.inputs[0])
    assemblymodulehole.links.new(reroute_001.outputs[0], vector_math_001.inputs[1])
    assemblymodulehole.links.new(reroute.outputs[0], reroute_008.inputs[0])
    assemblymodulehole.links.new(reroute_008.outputs[0], vector_math_020.inputs[0])
    assemblymodulehole.links.new(
        group_input_016.outputs[0], sample_nearest_surface_001.inputs[0]
    )
    assemblymodulehole.links.new(
        capture_attribute_005.outputs[0], delete_geometry.inputs[0]
    )
    assemblymodulehole.links.new(
        sample_nearest_surface_001.outputs[2], compare_002.inputs[5]
    )
    assemblymodulehole.links.new(
        capture_attribute_005.outputs[1], compare_002.inputs[4]
    )
    assemblymodulehole.links.new(compare_002.outputs[0], delete_geometry.inputs[1])
    assemblymodulehole.links.new(delete_geometry.outputs[0], mesh_boolean.inputs[1])
    assemblymodulehole.links.new(
        group_input_016.outputs[0], capture_attribute_005.inputs[0]
    )
    assemblymodulehole.links.new(normal_006.outputs[0], capture_attribute_005.inputs[1])
    assemblymodulehole.links.new(reroute_021.outputs[0], vector_math_021.inputs[0])
    assemblymodulehole.links.new(reroute_015.outputs[0], vector_rotate_001.inputs[0])
    assemblymodulehole.links.new(
        reroute_003.outputs[0], sample_nearest_surface_001.inputs[6]
    )
    assemblymodulehole.links.new(reroute_007.outputs[0], reroute_006.inputs[0])
    assemblymodulehole.links.new(vector_math_004.outputs[0], set_position_1.inputs[3])
    assemblymodulehole.links.new(math_001.outputs[0], vector_math_004.inputs[3])
    assemblymodulehole.links.new(group_input_004.outputs[12], math_001.inputs[0])
    assemblymodulehole.links.new(normal_001.outputs[0], capture_attribute_001.inputs[2])
    assemblymodulehole.links.new(normal_001.outputs[0], capture_attribute_001.inputs[1])
    assemblymodulehole.links.new(
        set_shade_smooth.outputs[0], capture_attribute_001.inputs[0]
    )
    assemblymodulehole.links.new(reroute_012.outputs[0], set_position_1.inputs[0])
    assemblymodulehole.links.new(
        capture_attribute_004.outputs[0], switch_002.inputs[14]
    )
    assemblymodulehole.links.new(mesh_boolean_001.outputs[0], switch.inputs[15])
    assemblymodulehole.links.new(switch.outputs[6], mesh_boolean_002.inputs[0])
    assemblymodulehole.links.new(group_input_2.outputs[0], switch.inputs[14])
    assemblymodulehole.links.new(group_input_2.outputs[13], switch.inputs[1])
    assemblymodulehole.links.new(vector_math_014.outputs[0], set_position_001.inputs[3])
    assemblymodulehole.links.new(normal_004.outputs[0], capture_attribute_003.inputs[2])
    assemblymodulehole.links.new(normal_004.outputs[0], capture_attribute_003.inputs[1])
    assemblymodulehole.links.new(reroute_016.outputs[0], set_position_001.inputs[0])
    assemblymodulehole.links.new(vector_math_015.outputs[0], vector_math_014.inputs[0])
    assemblymodulehole.links.new(group_input_014.outputs[15], math_002.inputs[1])
    assemblymodulehole.links.new(math_002.outputs[0], vector_math_014.inputs[3])
    assemblymodulehole.links.new(
        set_position_001.outputs[0], capture_attribute_004.inputs[0]
    )
    assemblymodulehole.links.new(
        capture_attribute_003.outputs[0], reroute_016.inputs[0]
    )
    assemblymodulehole.links.new(
        capture_attribute_001.outputs[0], reroute_012.inputs[0]
    )
    assemblymodulehole.links.new(reroute_007.outputs[0], vector_math_002.inputs[0])
    assemblymodulehole.links.new(math.outputs[0], vector_math_002.inputs[3])
    assemblymodulehole.links.new(
        vector_math_002.outputs[0], transform_geometry_001.inputs[1]
    )
    assemblymodulehole.links.new(set_position_002.outputs[0], switch_002.inputs[15])
    assemblymodulehole.links.new(reroute_010.outputs[0], vector_math_020.inputs[3])
    assemblymodulehole.links.new(reroute_017.outputs[0], vector_math_018.inputs[1])
    assemblymodulehole.links.new(
        capture_attribute_003.outputs[1], vector_math_018.inputs[0]
    )
    assemblymodulehole.links.new(
        capture_attribute_003.outputs[1], vector_math_016.inputs[0]
    )
    assemblymodulehole.links.new(vector_math_016.outputs[0], vector_math_015.inputs[0])
    assemblymodulehole.links.new(reroute_017.outputs[0], vector_math_017.inputs[0])
    assemblymodulehole.links.new(vector_math_017.outputs[0], vector_math_016.inputs[1])
    assemblymodulehole.links.new(vector_math_018.outputs[1], vector_math_017.inputs[3])
    assemblymodulehole.links.new(vector_math_006.outputs[0], vector_math_003.inputs[0])
    assemblymodulehole.links.new(vector_math_007.outputs[0], vector_math_006.inputs[1])
    assemblymodulehole.links.new(vector_math_005.outputs[1], vector_math_007.inputs[3])
    assemblymodulehole.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    assemblymodulehole.links.new(
        capture_attribute_001.outputs[1], vector_math_005.inputs[0]
    )
    assemblymodulehole.links.new(reroute_013.outputs[0], vector_math_005.inputs[1])
    assemblymodulehole.links.new(reroute_013.outputs[0], vector_math_007.inputs[0])
    assemblymodulehole.links.new(reroute_006.outputs[0], reroute_017.inputs[0])
    assemblymodulehole.links.new(reroute_006.outputs[0], reroute_013.inputs[0])
    assemblymodulehole.links.new(math_001.outputs[0], math_002.inputs[0])
    assemblymodulehole.links.new(
        convex_hull.outputs[0], transform_geometry_003.inputs[0]
    )
    assemblymodulehole.links.new(
        transform_geometry_003.outputs[0], transform_geometry_002.inputs[0]
    )
    assemblymodulehole.links.new(
        vector_math_002.outputs[0], transform_geometry_002.inputs[1]
    )
    assemblymodulehole.links.new(
        vector_math_001.outputs[0], transform_geometry_003.inputs[1]
    )
    assemblymodulehole.links.new(
        align_euler_to_vector.outputs[0], transform_geometry_003.inputs[2]
    )
    assemblymodulehole.links.new(
        is_shade_smooth.outputs[0], attribute_statistic_001.inputs[2]
    )
    assemblymodulehole.links.new(
        attribute_statistic_001.outputs[1], set_shade_smooth.inputs[2]
    )
    assemblymodulehole.links.new(
        capture_attribute_001.outputs[1], vector_math_006.inputs[0]
    )
    assemblymodulehole.links.new(normal_003.outputs[0], capture_attribute_002.inputs[1])
    assemblymodulehole.links.new(capture_attribute_002.outputs[1], compare.inputs[4])
    assemblymodulehole.links.new(
        capture_attribute_002.outputs[0], extrude_mesh.inputs[0]
    )
    assemblymodulehole.links.new(compare.outputs[0], extrude_mesh.inputs[1])
    assemblymodulehole.links.new(vector_math_013.outputs[0], extrude_mesh.inputs[2])
    assemblymodulehole.links.new(reroute_008.outputs[0], vector_math_013.inputs[0])
    assemblymodulehole.links.new(reroute_010.outputs[0], vector_math_013.inputs[3])
    assemblymodulehole.links.new(
        transform_geometry_002.outputs[0], capture_attribute_002.inputs[0]
    )
    assemblymodulehole.links.new(set_shade_smooth.outputs[0], switch_001.inputs[14])
    assemblymodulehole.links.new(switch_001.outputs[6], capture_attribute_003.inputs[0])
    assemblymodulehole.links.new(group_input_013.outputs[14], switch_001.inputs[1])
    assemblymodulehole.links.new(reroute_018.outputs[0], compare_003.inputs[5])
    assemblymodulehole.links.new(reroute_008.outputs[0], compare.inputs[5])
    assemblymodulehole.links.new(extrude_mesh.outputs[0], switch_001.inputs[15])
    assemblymodulehole.links.new(group_input_011.outputs[1], random_value_003.inputs[8])
    assemblymodulehole.links.new(integer_003.outputs[0], random_value_003.inputs[7])
    assemblymodulehole.links.new(random_value_003.outputs[1], combine_xyz_002.inputs[2])
    assemblymodulehole.links.new(
        reroute_027.outputs[0], transform_geometry_004.inputs[2]
    )
    assemblymodulehole.links.new(group_input_018.outputs[2], object_info_002.inputs[0])
    assemblymodulehole.links.new(group_001.outputs[0], transform_geometry_004.inputs[0])
    assemblymodulehole.links.new(group_input_012.outputs[8], random_value_003.inputs[2])
    assemblymodulehole.links.new(group_input_012.outputs[9], random_value_003.inputs[3])
    assemblymodulehole.links.new(
        transform_geometry_004.outputs[0], transform_geometry.inputs[0]
    )
    assemblymodulehole.links.new(
        transform_geometry_004.outputs[0], convex_hull.inputs[0]
    )
    assemblymodulehole.links.new(object_info_002.outputs[3], group_001.inputs[0])
    assemblymodulehole.links.new(group_input_019.outputs[2], object_info_003.inputs[0])
    assemblymodulehole.links.new(
        object_info_003.outputs[3], attribute_statistic_001.inputs[0]
    )
    assemblymodulehole.links.new(capture_attribute.outputs[1], compare_004.inputs[4])
    assemblymodulehole.links.new(compare_003.outputs[0], boolean_math.inputs[1])
    assemblymodulehole.links.new(compare_004.outputs[0], boolean_math.inputs[0])
    assemblymodulehole.links.new(reroute_008.outputs[0], reroute_018.inputs[0])
    assemblymodulehole.links.new(reroute_018.outputs[0], compare_004.inputs[5])
    assemblymodulehole.links.new(
        capture_attribute_004.outputs[0], set_position_002.inputs[0]
    )
    assemblymodulehole.links.new(compare_001.outputs[0], set_position_002.inputs[1])
    assemblymodulehole.links.new(group_input_020.outputs[15], vector_math_019.inputs[3])
    assemblymodulehole.links.new(reroute_019.outputs[0], vector_math_019.inputs[0])
    assemblymodulehole.links.new(vector_math_019.outputs[0], set_position_002.inputs[3])
    assemblymodulehole.links.new(reroute_026.outputs[0], vector_math_022.inputs[1])
    assemblymodulehole.links.new(vector_math_002.outputs[0], reroute_024.inputs[0])
    assemblymodulehole.links.new(reroute_024.outputs[0], reroute_025.inputs[0])
    assemblymodulehole.links.new(mesh_boolean_002.outputs[0], group_output_2.inputs[0])
    assemblymodulehole.links.new(reroute_022.outputs[0], vector_math_022.inputs[0])
    assemblymodulehole.links.new(reroute_023.outputs[0], reroute_026.inputs[0])
    assemblymodulehole.links.new(group_input_022.outputs[0], raycast.inputs[0])
    assemblymodulehole.links.new(reroute_026.outputs[0], vector_math_023.inputs[0])
    assemblymodulehole.links.new(vector_math_023.outputs[0], raycast.inputs[7])
    assemblymodulehole.links.new(vector_math_022.outputs[0], raycast.inputs[6])
    assemblymodulehole.links.new(raycast.outputs[1], group_output_2.inputs[1])
    assemblymodulehole.links.new(combine_xyz_002.outputs[0], reroute_027.inputs[0])
    assemblymodulehole.links.new(reroute_027.outputs[0], reroute_028.inputs[0])
    assemblymodulehole.links.new(mesh_boolean_002.outputs[0], raycast_001.inputs[0])
    assemblymodulehole.links.new(reroute_025.outputs[0], raycast_001.inputs[7])
    assemblymodulehole.links.new(raycast.outputs[1], raycast_001.inputs[6])
    assemblymodulehole.links.new(
        raycast_001.outputs[2], align_euler_to_vector_001.inputs[2]
    )
    assemblymodulehole.links.new(
        reroute_028.outputs[0], align_euler_to_vector_001.inputs[0]
    )
    assemblymodulehole.links.new(reroute_028.outputs[0], group_output_2.inputs[2])
    assemblymodulehole.links.new(
        align_euler_to_vector_001.outputs[0], group_output_2.inputs[4]
    )
    assemblymodulehole.links.new(raycast_001.outputs[1], group_output_2.inputs[3])
    assemblymodulehole.links.new(
        capture_attribute.outputs[0], set_position_003.inputs[0]
    )
    assemblymodulehole.links.new(compare_003.outputs[0], set_position_003.inputs[1])
    assemblymodulehole.links.new(vector_math_020.outputs[0], set_position_003.inputs[3])
    assemblymodulehole.links.new(
        set_position_003.outputs[0], set_shade_smooth.inputs[0]
    )
    assemblymodulehole.links.new(boolean_math.outputs[0], set_shade_smooth.inputs[1])
    return assemblymodulehole


assemblymodulehole = assemblymodulehole_node_group()
