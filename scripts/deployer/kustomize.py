class KustomizeDeployer():
    def __init__(self, shell, cluster):
        self.shell = shell
        self.cluster = cluster

    def deploy(self, dryrun=False):
        render_command = ["kustomize", "build", "kustomize", "--load_restrictor", "LoadRestrictionsNone", "-o", "rendered.yaml"]
        apply_command = ["kubectl", "apply", "-f", "rendered.yaml", "--context", self.cluster]

        if dryrun:
            apply_command.extend(["--dry-run=server"])
            
        self.shell.execute(render_command)
        self.shell.execute(apply_command)

    # TODO add ability to diff the manifest
    def diff(self):
        return
