import yaml
def read_yaml(yamlPath):
    with open(yamlPath,encoding='utf-8') as f:
        value=yaml.load(f,Loader=yaml.FullLoader)
        return value
if __name__ == '__main__':
    print(read_yaml())