import json
import hashlib
import os

def anonimze_users_in_file(file):
    # Check if file is JSON
    if not file.endswith("json"):
        return
    # Read in the JSON file
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)

    # Iterate through the data
    for item in data:
        if 'owner' in item:
            # Get the "id" element and generate a hash of it
            owner_id = item['owner']['id']
            owner_hash = hashlib.sha256(owner_id.encode()).hexdigest()
        
            # Replace the "owner" object with the hash value
            item['owner'] = owner_hash
        if 'answers' in item:
            for answer in item['answers']:
                if 'owner' in answer:
                    # Get the "id" element and generate a hash of it
                    owner_id = answer['owner']['id']
                    owner_hash = hashlib.sha256(owner_id.encode()).hexdigest()
                
                    # Replace the "owner" object with the hash value
                    answer['owner'] = owner_hash

    # Write the modified data back to the JSON file
    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f,indent=2, ensure_ascii=False)

if __name__ == "__main__":
    for file in os.listdir("./comments_json"):
        anonimze_users_in_file(f"./comments_json/{file}")