//! Generate peg-in-hole modules (test set).

use blr::prelude::*;
use pyo3::prelude::*;
use std::f64::consts::PI;

fn main() {
    Python::with_gil(|py| {
        let blend_project = BlendProject::empty(py).unwrap();

        // Load geometry nodes
        blr::utils::python::run_bpy_code(
            py,
            include_str!(concat!(
                env!("CARGO_MANIFEST_DIR"),
                "/nodes/module_blank.py"
            )),
        )
        .unwrap();
        blr::utils::python::run_bpy_code(
            py,
            include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/nodes/module_hole.py")),
        )
        .unwrap();
        blr::utils::python::run_bpy_code(
            py,
            include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/nodes/module_peg.py")),
        )
        .unwrap();

        // Peg
        let mut peg_module_object =
            blr::Object::new_mesh(py, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]).unwrap();
        let mut peg_module_mesh = blr::Mesh::try_from(&peg_module_object).unwrap();

        peg_module_object.set_name(py, "peg").unwrap();
        peg_module_mesh.set_name(py, "peg_mesh").unwrap();

        let mut modifier_module_peg =
            blr::modifiers::NodesModifier::new(py, &peg_module_object, "AssemblyModulePeg")
                .unwrap();
        modifier_module_peg
            .set_node_group_to(py, "AssemblyModulePeg")
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "profile_p_circle", 0.25)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "profile_n_vertices_circle", 32)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "radius_min", 0.02)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "radius_max", 0.03)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "height_min", 0.025)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "height_max", 0.15)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "aspect_ratio_min", 0.25)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "aspect_ratio_max", 1.0)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "taper_factor_min", 0.0)
            .unwrap();
        modifier_module_peg
            .set_input_attribute(py, "taper_factor_max", 0.25)
            .unwrap();

        let _modifier_triangulate_peg =
            blr::modifiers::TriangulateModifier::new(py, &peg_module_object, "TriangulateModifier")
                .unwrap();

        // Hole
        let mut hole_module_object =
            blr::Object::new_mesh(py, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]).unwrap();
        let mut hole_module_mesh = blr::Mesh::try_from(&hole_module_object).unwrap();

        hole_module_object.set_name(py, "hole").unwrap();
        hole_module_mesh.set_name(py, "hole_mesh").unwrap();

        let mut modifier_module_blank =
            blr::modifiers::NodesModifier::new(py, &hole_module_object, "AssemblyModuleBlank")
                .unwrap();
        modifier_module_blank
            .set_node_group_to(py, "AssemblyModuleBlank")
            .unwrap();
        modifier_module_blank
            .set_input_attribute(py, "module_thickness", 0.005)
            .unwrap();
        modifier_module_blank
            .set_input_attribute(py, "module_size_tolerance", 0.000)
            .unwrap();
        modifier_module_blank
            .set_input_attribute(py, "holes_enable", false)
            .unwrap();

        let mut modifier_module_hole =
            blr::modifiers::NodesModifier::new(py, &hole_module_object, "AssemblyModuleHole")
                .unwrap();
        modifier_module_hole
            .set_node_group_to(py, "AssemblyModuleHole")
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "peg", &peg_module_object)
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_depth_factor_min", 0.4)
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_depth_factor_max", 0.8)
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_position_offset_min", [-0.025, -0.025, 0.0])
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_position_offset_max", [0.025, 0.025, 0.0])
            .unwrap();
        modifier_module_hole
            .set_input_attribute(
                py,
                "hole_orientation_offset_min",
                [-PI / 12.0, -PI / 12.0, -PI],
            )
            .unwrap();
        modifier_module_hole
            .set_input_attribute(
                py,
                "hole_orientation_offset_max",
                [PI / 12.0, PI / 12.0, PI],
            )
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_insertion_angle_min", -PI)
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_insertion_angle_max", PI)
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "hole_size_tolerance", 0.001)
            .unwrap();
        modifier_module_hole
            .set_input_attribute(py, "wall_thickness", 0.005)
            .unwrap();

        let _modifier_triangulate_hole = blr::modifiers::TriangulateModifier::new(
            py,
            &hole_module_object,
            "TriangulateModifier",
        )
        .unwrap();

        modifier_module_hole
            .set_output_attribute_name(py, "entrance_position", "entrance_position")
            .unwrap();
        modifier_module_hole
            .set_output_attribute_name(py, "entrance_orientation", "entrance_orientation")
            .unwrap();
        modifier_module_hole
            .set_output_attribute_name(py, "bottom_position", "bottom_position")
            .unwrap();
        modifier_module_hole
            .set_output_attribute_name(py, "bottom_orientation", "bottom_orientation")
            .unwrap();

        let mut empty_entrance =
            blr::Object::new_empty(py, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]).unwrap();
        empty_entrance.set_name(py, "entrance").unwrap();
        empty_entrance.set_parent(py, &hole_module_object).unwrap();
        let mut empty_bottom =
            blr::Object::new_empty(py, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]).unwrap();
        empty_bottom.set_name(py, "bottom").unwrap();
        empty_bottom.set_parent(py, &hole_module_object).unwrap();

        const INITIAL_SEED: isize = 2048;
        const N_OBJECTS_TO_GENERATE: isize = 1024;
        for i in 0..N_OBJECTS_TO_GENERATE {
            let mesh_path = std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"))
                .parent()
                .unwrap()
                .join("assets")
                .join("test")
                .join("meshes")
                .join(format!("peg_in_hole_module_{i}.usdc",));
            println!("Exporting '{}' ...", mesh_path.display());

            modifier_module_peg
                .set_input_attribute(py, "random_seed", INITIAL_SEED + i)
                .unwrap();
            modifier_module_hole
                .set_input_attribute(py, "random_seed", INITIAL_SEED + i)
                .unwrap();

            // Trigger recalculation of the modifiers via update
            peg_module_mesh.update(py, true, true).unwrap();
            hole_module_mesh.update(py, true, true).unwrap();

            let entrance_position: [f32; 3] = hole_module_mesh
                .get_output_attribute_data(py, "entrance_position")
                .unwrap()
                .into_py(py)
                .extract(py)
                .unwrap();
            let entrance_orientation: [f32; 3] = hole_module_mesh
                .get_output_attribute_data(py, "entrance_orientation")
                .unwrap()
                .into_py(py)
                .extract(py)
                .unwrap();
            empty_entrance.set_location(py, entrance_position).unwrap();
            empty_entrance
                .set_rotation_euler(py, entrance_orientation)
                .unwrap();

            let bottom_position: [f32; 3] = hole_module_mesh
                .get_output_attribute_data(py, "bottom_position")
                .unwrap()
                .into_py(py)
                .extract(py)
                .unwrap();
            let bottom_orientation: [f32; 3] = hole_module_mesh
                .get_output_attribute_data(py, "bottom_orientation")
                .unwrap()
                .into_py(py)
                .extract(py)
                .unwrap();
            empty_bottom.set_location(py, bottom_position).unwrap();
            empty_bottom
                .set_rotation_euler(py, bottom_orientation)
                .unwrap();

            // Export as USD
            blend_project
                .export(
                    blr::export::UsdExporterBuilder::default()
                        .selected_objects_only(false)
                        .export_materials(false)
                        .root_prim_path("/module")
                        .build(),
                    &mesh_path,
                )
                .unwrap();
        }
    });
}
