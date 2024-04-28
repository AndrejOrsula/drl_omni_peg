use pyo3_bindgen::Codegen;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Generate Rust bindings to Python modules
    Codegen::default()
        .module_name("gymnasium")?
        .build(std::path::Path::new(&std::env::var("OUT_DIR")?).join("bindings_gymnasium.rs"))?;
    Codegen::default()
        .module_name("dreamerv3")?
        .build(std::path::Path::new(&std::env::var("OUT_DIR")?).join("bindings_dreamerv3.rs"))?;
    Codegen::default()
        .module_names(["stable_baselines3", "sb3_contrib"])?
        .build(std::path::Path::new(&std::env::var("OUT_DIR")?).join("bindings_sb3.rs"))?;
    Ok(())
}
