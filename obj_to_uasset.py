import unreal
import argparse

def obj_to_uasset(obj_path, uasset_path):
    """
    Converts a .obj file to a .uasset in Unreal Engine.
    
    """
 
    if not hasattr(unreal, 'AssetToolsHelpers'):
        raise RuntimeError("This script must be run inside Unreal Editor's Python environment.")

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    
    import_task = unreal.AssetImportTask()
    import_task.filename = obj_path
    import_task.destination_path = uasset_path
    import_task.automated = True  # Suppress UI dialogs
    import_task.replace_existing = True  # Overwrite existing assets
    import_task.save = True  # Save the asset after import
    
    print(f"Importing {obj_path} to {uasset_path}")
    asset_tools.import_asset_tasks([import_task])
    print(f"Imported {obj_path} to {uasset_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .obj to .uasset in Unreal Engine")
    parser.add_argument('--obj_path', type=str, required=True, help='Path to the .obj file')
    parser.add_argument('--uasset_path', type=str, required=True, help='Destination path in Unreal Engine (e.g., "/Game/MyFolder")')
    args = parser.parse_args()
    obj_path = args.obj_path
    uasset_path = args.uasset_path
    obj_to_uasset(obj_path, uasset_path)
