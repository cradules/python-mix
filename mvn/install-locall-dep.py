import json
import subprocess


def install_maven_dependency(command_info):
    cmd = [
        "mvn", "install:install-file",
        "-DgroupId={}".format(command_info["groupId"]),
        "-DartifactId={}".format(command_info["artifactId"]),
        "-Dversion={}".format(command_info["version"]),
        "-Dpackaging={}".format(command_info["packaging"]),
        "-Dfile={}".format(command_info["file"]),
    ]

    if "pomFile" in command_info:
        cmd.extend(["-DpomFile={}".format(command_info["pomFile"])])

    subprocess.run(cmd, check=True)


def main():
    with open("local_dep.json") as f:
        config = json.load(f)

    for command_info in config["commands"]:
        install_maven_dependency(command_info)


if __name__ == "__main__":
    main()
