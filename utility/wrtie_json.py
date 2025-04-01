import json

async def write_on_json_file(p_json_file, p_data):
    try:
        with open(p_json_file, "w") as file:
            json.dump(p_data, file, indent=4, sort_keys=True)
    except Exception as e:
        print(f"Erreur lors de l'ecriture du fichier {p_json_file} : {e}")


def get_data_from_json_file(p_json_file):
    try:
        with open(p_json_file) as file:
            return json.load(file)
    except:
        return []
