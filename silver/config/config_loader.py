def load_config(path):
    config = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if '=' in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config
