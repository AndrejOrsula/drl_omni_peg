def assemblymodulepeg_node_group():
    assemblymodulepeg = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="AssemblyModulePeg"
    )

    frame = assemblymodulepeg.nodes.new("NodeFrame")
    frame.label = "Peg Profile (N-Gon/Circle)"

    frame_001 = assemblymodulepeg.nodes.new("NodeFrame")
    frame_001.label = "Base geometry"

    frame_002 = assemblymodulepeg.nodes.new("NodeFrame")
    frame_002.label = "Refine Shape (Aspect Ratio)"

    frame_003 = assemblymodulepeg.nodes.new("NodeFrame")
    frame_003.label = "Peg Height"

    frame_004 = assemblymodulepeg.nodes.new("NodeFrame")
    frame_004.label = "Peg Radius: top"

    frame_005 = assemblymodulepeg.nodes.new("NodeFrame")
    frame_005.label = "Peg Radius: bottom (tapering)"

    frame_006 = assemblymodulepeg.nodes.new("NodeFrame")
    frame_006.label = "Make the geometry uniform"

    switch = assemblymodulepeg.nodes.new("GeometryNodeSwitch")
    switch.input_type = "INT"
    switch.inputs[1].default_value = False
    switch.inputs[2].default_value = 0.0
    switch.inputs[3].default_value = 0.0
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

    assemblymodulepeg.inputs.new("NodeSocketInt", "random_seed")
    assemblymodulepeg.inputs[0].default_value = 0
    assemblymodulepeg.inputs[0].min_value = 0
    assemblymodulepeg.inputs[0].max_value = 2147483647
    assemblymodulepeg.inputs[0].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatFactor", "profile_p_circle")
    assemblymodulepeg.inputs[1].default_value = 0.25
    assemblymodulepeg.inputs[1].min_value = 0.0
    assemblymodulepeg.inputs[1].max_value = 1.0
    assemblymodulepeg.inputs[1].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketInt", "profile_n_vertices_circle")
    assemblymodulepeg.inputs[2].default_value = 16
    assemblymodulepeg.inputs[2].min_value = 3
    assemblymodulepeg.inputs[2].max_value = 2147483647
    assemblymodulepeg.inputs[2].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketInt", "profile_n_vertices_ngon_min")
    assemblymodulepeg.inputs[3].default_value = 3
    assemblymodulepeg.inputs[3].min_value = 3
    assemblymodulepeg.inputs[3].max_value = 2147483647
    assemblymodulepeg.inputs[3].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketInt", "profile_n_vertices_ngon_max")
    assemblymodulepeg.inputs[4].default_value = 8
    assemblymodulepeg.inputs[4].min_value = 3
    assemblymodulepeg.inputs[4].max_value = 2147483647
    assemblymodulepeg.inputs[4].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatDistance", "radius_min")
    assemblymodulepeg.inputs[5].default_value = 0.009999999776482582
    assemblymodulepeg.inputs[5].min_value = 0.0
    assemblymodulepeg.inputs[5].max_value = 3.4028234663852886e38
    assemblymodulepeg.inputs[5].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatDistance", "radius_max")
    assemblymodulepeg.inputs[6].default_value = 0.02500000037252903
    assemblymodulepeg.inputs[6].min_value = 0.0
    assemblymodulepeg.inputs[6].max_value = 3.4028234663852886e38
    assemblymodulepeg.inputs[6].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatDistance", "height_min")
    assemblymodulepeg.inputs[7].default_value = 0.03999999910593033
    assemblymodulepeg.inputs[7].min_value = 0.0
    assemblymodulepeg.inputs[7].max_value = 3.4028234663852886e38
    assemblymodulepeg.inputs[7].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatDistance", "height_max")
    assemblymodulepeg.inputs[8].default_value = 0.07999999821186066
    assemblymodulepeg.inputs[8].min_value = 0.0
    assemblymodulepeg.inputs[8].max_value = 3.4028234663852886e38
    assemblymodulepeg.inputs[8].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatFactor", "aspect_ratio_min")
    assemblymodulepeg.inputs[9].default_value = 1.0
    assemblymodulepeg.inputs[9].min_value = 0.0
    assemblymodulepeg.inputs[9].max_value = 1.0
    assemblymodulepeg.inputs[9].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatFactor", "aspect_ratio_max")
    assemblymodulepeg.inputs[10].default_value = 1.0
    assemblymodulepeg.inputs[10].min_value = 0.0
    assemblymodulepeg.inputs[10].max_value = 1.0
    assemblymodulepeg.inputs[10].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatFactor", "taper_factor_min")
    assemblymodulepeg.inputs[11].default_value = 0.0
    assemblymodulepeg.inputs[11].min_value = 0.0
    assemblymodulepeg.inputs[11].max_value = 0.9990000128746033
    assemblymodulepeg.inputs[11].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketFloatFactor", "taper_factor_max")
    assemblymodulepeg.inputs[12].default_value = 0.0
    assemblymodulepeg.inputs[12].min_value = 0.0
    assemblymodulepeg.inputs[12].max_value = 0.9990000128746033
    assemblymodulepeg.inputs[12].attribute_domain = "POINT"

    assemblymodulepeg.inputs.new("NodeSocketBool", "use_uniform_geometry")
    assemblymodulepeg.inputs[13].default_value = False
    assemblymodulepeg.inputs[13].attribute_domain = "POINT"

    group_input = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True
    group_input.outputs[7].hide = True
    group_input.outputs[8].hide = True
    group_input.outputs[9].hide = True
    group_input.outputs[10].hide = True
    group_input.outputs[11].hide = True
    group_input.outputs[12].hide = True
    group_input.outputs[13].hide = True
    group_input.outputs[14].hide = True

    integer = assemblymodulepeg.nodes.new("FunctionNodeInputInt")

    group_input_001 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
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

    random_value = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value.data_type = "BOOLEAN"
    random_value.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value.inputs[2].default_value = 0.0
    random_value.inputs[3].default_value = 1.0
    random_value.inputs[4].default_value = 0
    random_value.inputs[5].default_value = 100

    group_input_002 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
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

    random_value_001 = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value_001.data_type = "INT"
    random_value_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value_001.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value_001.inputs[2].default_value = 0.0
    random_value_001.inputs[3].default_value = 1.0
    random_value_001.inputs[6].default_value = 0.5

    group_input_003 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True
    group_input_003.outputs[11].hide = True
    group_input_003.outputs[12].hide = True
    group_input_003.outputs[13].hide = True
    group_input_003.outputs[14].hide = True

    integer_001 = assemblymodulepeg.nodes.new("FunctionNodeInputInt")
    integer_001.integer = 1

    group_input_004 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True

    reroute = assemblymodulepeg.nodes.new("NodeReroute")
    reroute.label = "is_circle"
    math = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math.operation = "MULTIPLY"
    math.inputs[0].hide = True
    math.inputs[2].hide = True
    math.inputs[0].default_value = -0.5
    math.inputs[2].default_value = 0.5

    combine_xyz = assemblymodulepeg.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.inputs[0].hide = True
    combine_xyz.inputs[1].hide = True
    combine_xyz.inputs[0].default_value = 0.0
    combine_xyz.inputs[1].default_value = 0.0

    scale_elements = assemblymodulepeg.nodes.new("GeometryNodeScaleElements")
    scale_elements.domain = "FACE"
    scale_elements.scale_mode = "SINGLE_AXIS"
    scale_elements.inputs[1].default_value = True
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)

    integer_002 = assemblymodulepeg.nodes.new("FunctionNodeInputInt")
    integer_002.integer = 5

    group_input_005 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
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

    random_value_002 = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value_002.data_type = "FLOAT"
    random_value_002.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value_002.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value_002.inputs[4].default_value = 3
    random_value_002.inputs[5].default_value = 10
    random_value_002.inputs[6].default_value = 0.5

    group_input_006 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True

    random_value_003 = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value_003.data_type = "FLOAT_VECTOR"
    random_value_003.inputs[0].default_value = (-1.0, -1.0, 0.0)
    random_value_003.inputs[1].default_value = (1.0, 1.0, 0.0)
    random_value_003.inputs[2].default_value = 0.0
    random_value_003.inputs[3].default_value = 1.0
    random_value_003.inputs[4].default_value = 3
    random_value_003.inputs[5].default_value = 10
    random_value_003.inputs[6].default_value = 0.5

    group_input_007 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[11].hide = True
    group_input_007.outputs[12].hide = True
    group_input_007.outputs[13].hide = True
    group_input_007.outputs[14].hide = True

    assemblymodulepeg.outputs.new("NodeSocketGeometry", "Geometry")
    assemblymodulepeg.outputs[0].attribute_domain = "POINT"

    group_output = assemblymodulepeg.nodes.new("NodeGroupOutput")
    group_output.inputs[1].hide = True

    set_shade_smooth = assemblymodulepeg.nodes.new("GeometryNodeSetShadeSmooth")

    integer_003 = assemblymodulepeg.nodes.new("FunctionNodeInputInt")
    integer_003.integer = 6

    transform_geometry = assemblymodulepeg.nodes.new("GeometryNodeTransform")
    transform_geometry.mute = True
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    cone = assemblymodulepeg.nodes.new("GeometryNodeMeshCone")
    cone.fill_type = "NGON"

    group_input_008 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    group_input_008.outputs[11].hide = True
    group_input_008.outputs[12].hide = True
    group_input_008.outputs[13].hide = True
    group_input_008.outputs[14].hide = True

    integer_004 = assemblymodulepeg.nodes.new("FunctionNodeInputInt")
    integer_004.integer = 3

    group_input_009 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    group_input_009.outputs[11].hide = True
    group_input_009.outputs[12].hide = True
    group_input_009.outputs[13].hide = True
    group_input_009.outputs[14].hide = True

    random_value_004 = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value_004.data_type = "FLOAT"
    random_value_004.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value_004.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value_004.inputs[4].default_value = 3
    random_value_004.inputs[5].default_value = 10
    random_value_004.inputs[6].default_value = 0.5

    group_input_010 = assemblymodulepeg.nodes.new("NodeGroupInput")
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

    integer_005 = assemblymodulepeg.nodes.new("FunctionNodeInputInt")
    integer_005.integer = 2

    group_input_011 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[1].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[4].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True

    random_value_005 = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value_005.data_type = "FLOAT"
    random_value_005.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value_005.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value_005.inputs[4].default_value = 3
    random_value_005.inputs[5].default_value = 10
    random_value_005.inputs[6].default_value = 0.5

    math_001 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_001.operation = "SUBTRACT"
    math_001.inputs[0].default_value = 1.0
    math_001.inputs[2].default_value = 0.5

    math_002 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_002.operation = "MULTIPLY"
    math_002.inputs[2].default_value = 0.5

    group_input_012 = assemblymodulepeg.nodes.new("NodeGroupInput")
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True
    group_input_012.outputs[13].hide = True
    group_input_012.outputs[14].hide = True

    integer_006 = assemblymodulepeg.nodes.new("FunctionNodeInputInt")
    integer_006.integer = 4

    group_input_013 = assemblymodulepeg.nodes.new("NodeGroupInput")
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
    group_input_013.outputs[14].hide = True

    random_value_006 = assemblymodulepeg.nodes.new("FunctionNodeRandomValue")
    random_value_006.data_type = "FLOAT"
    random_value_006.inputs[0].default_value = (0.0, 0.0, 0.0)
    random_value_006.inputs[1].default_value = (1.0, 1.0, 1.0)
    random_value_006.inputs[4].default_value = 3
    random_value_006.inputs[5].default_value = 10
    random_value_006.inputs[6].default_value = 0.5

    reroute_001 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_001.label = "Radius"
    reroute_002 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_003 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_003.label = "Vertices"
    reroute_004 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_004.label = "Height"
    reroute_005 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_006 = assemblymodulepeg.nodes.new("NodeReroute")
    math_003 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_003.operation = "DIVIDE"
    math_003.inputs[2].default_value = 0.5

    math_004 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_004.operation = "DIVIDE"
    math_004.inputs[2].default_value = 0.5

    math_005 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_005.operation = "CEIL"
    math_005.inputs[1].default_value = 0.5
    math_005.inputs[2].default_value = 0.5

    switch_001 = assemblymodulepeg.nodes.new("GeometryNodeSwitch")
    switch_001.input_type = "INT"
    switch_001.inputs[1].default_value = False
    switch_001.inputs[2].default_value = 0.0
    switch_001.inputs[3].default_value = 0.0
    switch_001.inputs[4].default_value = 1
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

    math_006 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_006.operation = "CEIL"
    math_006.inputs[1].default_value = 0.5
    math_006.inputs[2].default_value = 0.5

    group_input_014 = assemblymodulepeg.nodes.new("NodeGroupInput")
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
    group_input_014.outputs[14].hide = True

    switch_002 = assemblymodulepeg.nodes.new("GeometryNodeSwitch")
    switch_002.input_type = "INT"
    switch_002.inputs[1].default_value = False
    switch_002.inputs[2].default_value = 0.0
    switch_002.inputs[3].default_value = 0.0
    switch_002.inputs[4].default_value = 1
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

    math_007 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_007.operation = "MULTIPLY"
    math_007.inputs[1].default_value = 6.2831854820251465
    math_007.inputs[2].default_value = 0.5

    math_008 = assemblymodulepeg.nodes.new("ShaderNodeMath")
    math_008.operation = "DIVIDE"
    math_008.inputs[2].default_value = 0.5

    reroute_007 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_007.label = "Circumference"
    reroute_008 = assemblymodulepeg.nodes.new("NodeReroute")
    reroute_008.label = "Vertex per meter"
    switch.parent = frame
    group_input.parent = frame
    integer.parent = frame
    group_input_001.parent = frame
    random_value.parent = frame
    group_input_002.parent = frame
    random_value_001.parent = frame
    group_input_003.parent = frame
    integer_001.parent = frame
    group_input_004.parent = frame
    math.parent = frame_001
    combine_xyz.parent = frame_001
    scale_elements.parent = frame_002
    integer_002.parent = frame_002
    group_input_005.parent = frame_002
    random_value_002.parent = frame_002
    group_input_006.parent = frame_002
    random_value_003.parent = frame_002
    group_input_007.parent = frame_002
    integer_003.parent = frame_002
    transform_geometry.parent = frame_001
    cone.parent = frame_001
    group_input_008.parent = frame_003
    integer_004.parent = frame_003
    group_input_009.parent = frame_003
    random_value_004.parent = frame_003
    group_input_010.parent = frame_004
    integer_005.parent = frame_004
    group_input_011.parent = frame_004
    random_value_005.parent = frame_005
    math_001.parent = frame_005
    math_002.parent = frame_005
    group_input_012.parent = frame_005
    integer_006.parent = frame_005
    group_input_013.parent = frame_005
    random_value_006.parent = frame_004
    math_003.parent = frame_006
    math_004.parent = frame_006
    math_005.parent = frame_006
    switch_001.parent = frame_006
    math_006.parent = frame_006
    group_input_014.parent = frame_006
    switch_002.parent = frame_006
    math_007.parent = frame_006
    math_008.parent = frame_006
    reroute_007.parent = frame_006
    reroute_008.parent = frame_006

    frame.location = (-2364.13134765625, 475.01434326171875)
    frame_001.location = (757.2171020507812, 359.275146484375)
    frame_002.location = (1188.4765625, 284.1412353515625)
    frame_003.location = (-1824.343505859375, -462.14923095703125)
    frame_004.location = (-2608.612548828125, -299.5426025390625)
    frame_005.location = (-1215.678955078125, -47.47259521484375)
    frame_006.location = (-264.650146484375, 222.4400634765625)
    switch.location = (-237.70013427734375, 166.01531982421875)
    group_input.location = (-723.4949340820312, 200.67462158203125)
    integer.location = (-723.4949340820312, 295.67462158203125)
    group_input_001.location = (-723.4949340820312, 362.67462158203125)
    random_value.location = (-477.853759765625, 293.44110107421875)
    group_input_002.location = (-477.853759765625, -99.47715759277344)
    random_value_001.location = (-477.853759765625, 88.5228271484375)
    group_input_003.location = (-723.4949340820312, -93.69970703125)
    integer_001.location = (-723.4949340820312, 1.30029296875)
    group_input_004.location = (-723.4949340820312, 90.30029296875)
    reroute.location = (-201.34002685546875, 723.4322509765625)
    math.location = (-1397.6171875, -383.7940673828125)
    combine_xyz.location = (-1219.19677734375, -358.5167236328125)
    scale_elements.location = (-426.781494140625, 45.8795166015625)
    integer_002.location = (-891.415771484375, -128.57574462890625)
    group_input_005.location = (-891.415771484375, -223.57574462890625)
    random_value_002.location = (-645.774658203125, -79.97119140625)
    group_input_006.location = (-891.415771484375, -528.1066284179688)
    random_value_003.location = (-645.774658203125, -292.082275390625)
    group_input_007.location = (-891.415771484375, -39.57568359375)
    group_output.location = (1099.36865234375, 331.6226806640625)
    set_shade_smooth.location = (41.69342041015625, 308.8958740234375)
    integer_003.location = (-891.415771484375, -433.10662841796875)
    transform_geometry.location = (-1027.566650390625, -12.72100830078125)
    cone.location = (-1400.453125, -39.529327392578125)
    group_input_008.location = (-891.415771484375, -175.932861328125)
    integer_004.location = (-891.415771484375, -264.932861328125)
    group_input_009.location = (-891.415771484375, -359.932861328125)
    random_value_004.location = (-645.7745971679688, -216.32830810546875)
    group_input_010.location = (-896.7049560546875, -34.74586486816406)
    integer_005.location = (-896.7049560546875, 60.25413513183594)
    group_input_011.location = (-896.7049560546875, 149.25413513183594)
    random_value_005.location = (-1479.693603515625, -280.1707763671875)
    math_001.location = (-1289.693603515625, -289.6707763671875)
    math_002.location = (-1059.5533447265625, -268.74444580078125)
    group_input_012.location = (-1669.693603515625, -242.329833984375)
    integer_006.location = (-1669.693603515625, -331.329833984375)
    group_input_013.location = (-1669.693603515625, -426.329833984375)
    random_value_006.location = (-651.063720703125, 105.62535095214844)
    reroute_001.location = (-2987.373046875, -228.5765380859375)
    reroute_002.location = (-974.951416015625, 606.3013305664062)
    reroute_003.location = (-2168.303466796875, 606.7763671875)
    reroute_004.location = (-2240.54443359375, -715.2064819335938)
    reroute_005.location = (-1903.29833984375, -714.4459838867188)
    reroute_006.location = (-2367.25, -228.5765380859375)
    math_003.location = (-1266.7904052734375, 298.87701416015625)
    math_004.location = (-1266.7904052734375, 34.935150146484375)
    math_005.location = (-1076.7904052734375, 287.87701416015625)
    switch_001.location = (-886.7904052734375, 298.37701416015625)
    math_006.location = (-1076.7904052734375, 23.935150146484375)
    group_input_014.location = (-1076.7904052734375, 113.1856689453125)
    switch_002.location = (-886.7904052734375, 34.435150146484375)
    math_007.location = (-1901.017578125, 42.23974609375)
    math_008.location = (-1586.1864013671875, 121.13839721679688)
    reroute_007.location = (-1719.8779296875, 7.324859619140625)
    reroute_008.location = (-1394.48095703125, 87.21310424804688)

    frame.width, frame.height = 685.684326171875, 584.1842041015625
    frame_001.width, frame_001.height = 572.947265625, 570.9210205078125
    frame_002.width, frame_002.height = 663.8947143554688, 696.9210205078125
    frame_003.width, frame_003.height = 446.0, 304.7105712890625
    frame_004.width, frame_004.height = 445.052734375, 304.71051025390625
    frame_005.width, frame_005.height = 809.789306640625, 304.71051025390625
    frame_006.width, frame_006.height = 1214.31591796875, 488.5
    switch.width, switch.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    reroute.width, reroute.height = 16.0, 100.0
    math.width, math.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    integer_002.width, integer_002.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    random_value_003.width, random_value_003.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    integer_003.width, integer_003.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    cone.width, cone.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    integer_004.width, integer_004.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    random_value_004.width, random_value_004.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    integer_005.width, integer_005.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    random_value_005.width, random_value_005.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    integer_006.width, integer_006.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    random_value_006.width, random_value_006.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    reroute_003.width, reroute_003.height = 16.0, 100.0
    reroute_004.width, reroute_004.height = 16.0, 100.0
    reroute_005.width, reroute_005.height = 16.0, 100.0
    reroute_006.width, reroute_006.height = 16.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    reroute_007.width, reroute_007.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0

    assemblymodulepeg.links.new(group_input_003.outputs[0], random_value_001.inputs[8])
    assemblymodulepeg.links.new(integer_001.outputs[0], random_value_001.inputs[7])
    assemblymodulepeg.links.new(group_input.outputs[0], random_value.inputs[8])
    assemblymodulepeg.links.new(integer.outputs[0], random_value.inputs[7])
    assemblymodulepeg.links.new(random_value_001.outputs[2], switch.inputs[4])
    assemblymodulepeg.links.new(random_value.outputs[3], switch.inputs[0])
    assemblymodulepeg.links.new(integer_005.outputs[0], random_value_006.inputs[7])
    assemblymodulepeg.links.new(group_input_010.outputs[0], random_value_006.inputs[8])
    assemblymodulepeg.links.new(integer_004.outputs[0], random_value_004.inputs[7])
    assemblymodulepeg.links.new(group_input_009.outputs[0], random_value_004.inputs[8])
    assemblymodulepeg.links.new(group_input_011.outputs[5], random_value_006.inputs[2])
    assemblymodulepeg.links.new(group_input_008.outputs[7], random_value_004.inputs[2])
    assemblymodulepeg.links.new(group_input_002.outputs[2], switch.inputs[5])
    assemblymodulepeg.links.new(group_input_001.outputs[1], random_value.inputs[6])
    assemblymodulepeg.links.new(group_input_004.outputs[3], random_value_001.inputs[4])
    assemblymodulepeg.links.new(random_value.outputs[3], reroute.inputs[0])
    assemblymodulepeg.links.new(reroute.outputs[0], set_shade_smooth.inputs[2])
    assemblymodulepeg.links.new(
        transform_geometry.outputs[0], set_shade_smooth.inputs[0]
    )
    assemblymodulepeg.links.new(math_001.outputs[0], math_002.inputs[1])
    assemblymodulepeg.links.new(math_002.outputs[0], cone.inputs[4])
    assemblymodulepeg.links.new(cone.outputs[3], set_shade_smooth.inputs[1])
    assemblymodulepeg.links.new(cone.outputs[0], transform_geometry.inputs[0])
    assemblymodulepeg.links.new(combine_xyz.outputs[0], transform_geometry.inputs[1])
    assemblymodulepeg.links.new(math.outputs[0], combine_xyz.inputs[2])
    assemblymodulepeg.links.new(random_value_004.outputs[1], reroute_004.inputs[0])
    assemblymodulepeg.links.new(reroute_005.outputs[0], math.inputs[1])
    assemblymodulepeg.links.new(reroute_005.outputs[0], cone.inputs[5])
    assemblymodulepeg.links.new(reroute_006.outputs[0], cone.inputs[3])
    assemblymodulepeg.links.new(random_value_006.outputs[1], reroute_001.inputs[0])
    assemblymodulepeg.links.new(switch.outputs[1], reroute_003.inputs[0])
    assemblymodulepeg.links.new(reroute_002.outputs[0], cone.inputs[0])
    assemblymodulepeg.links.new(reroute_006.outputs[0], math_002.inputs[0])
    assemblymodulepeg.links.new(scale_elements.outputs[0], group_output.inputs[0])
    assemblymodulepeg.links.new(integer_002.outputs[0], random_value_002.inputs[7])
    assemblymodulepeg.links.new(group_input_005.outputs[0], random_value_002.inputs[8])
    assemblymodulepeg.links.new(group_input_007.outputs[9], random_value_002.inputs[2])
    assemblymodulepeg.links.new(group_input_007.outputs[10], random_value_002.inputs[3])
    assemblymodulepeg.links.new(group_input_008.outputs[8], random_value_004.inputs[3])
    assemblymodulepeg.links.new(group_input_011.outputs[6], random_value_006.inputs[3])
    assemblymodulepeg.links.new(group_input_004.outputs[4], random_value_001.inputs[5])
    assemblymodulepeg.links.new(set_shade_smooth.outputs[0], scale_elements.inputs[0])
    assemblymodulepeg.links.new(random_value_002.outputs[1], scale_elements.inputs[2])
    assemblymodulepeg.links.new(integer_003.outputs[0], random_value_003.inputs[7])
    assemblymodulepeg.links.new(group_input_006.outputs[0], random_value_003.inputs[8])
    assemblymodulepeg.links.new(random_value_003.outputs[0], scale_elements.inputs[4])
    assemblymodulepeg.links.new(integer_006.outputs[0], random_value_005.inputs[7])
    assemblymodulepeg.links.new(group_input_013.outputs[0], random_value_005.inputs[8])
    assemblymodulepeg.links.new(group_input_012.outputs[11], random_value_005.inputs[2])
    assemblymodulepeg.links.new(group_input_012.outputs[12], random_value_005.inputs[3])
    assemblymodulepeg.links.new(random_value_005.outputs[1], math_001.inputs[1])
    assemblymodulepeg.links.new(reroute_001.outputs[0], reroute_006.inputs[0])
    assemblymodulepeg.links.new(reroute_007.outputs[0], math_008.inputs[0])
    assemblymodulepeg.links.new(reroute_003.outputs[0], math_008.inputs[1])
    assemblymodulepeg.links.new(reroute_005.outputs[0], math_003.inputs[0])
    assemblymodulepeg.links.new(reroute_008.outputs[0], math_003.inputs[1])
    assemblymodulepeg.links.new(math_003.outputs[0], math_005.inputs[0])
    assemblymodulepeg.links.new(switch_001.outputs[1], cone.inputs[1])
    assemblymodulepeg.links.new(reroute_008.outputs[0], math_004.inputs[1])
    assemblymodulepeg.links.new(math_004.outputs[0], math_006.inputs[0])
    assemblymodulepeg.links.new(math_005.outputs[0], switch_001.inputs[5])
    assemblymodulepeg.links.new(math_006.outputs[0], switch_002.inputs[5])
    assemblymodulepeg.links.new(switch_002.outputs[1], cone.inputs[2])
    assemblymodulepeg.links.new(group_input_014.outputs[13], switch_001.inputs[0])
    assemblymodulepeg.links.new(group_input_014.outputs[13], switch_002.inputs[0])
    assemblymodulepeg.links.new(reroute_003.outputs[0], reroute_002.inputs[0])
    assemblymodulepeg.links.new(math_007.outputs[0], reroute_007.inputs[0])
    assemblymodulepeg.links.new(reroute_006.outputs[0], math_007.inputs[0])
    assemblymodulepeg.links.new(reroute_006.outputs[0], math_004.inputs[0])
    assemblymodulepeg.links.new(reroute_004.outputs[0], reroute_005.inputs[0])
    assemblymodulepeg.links.new(math_008.outputs[0], reroute_008.inputs[0])
    return assemblymodulepeg


assemblymodulepeg = assemblymodulepeg_node_group()
