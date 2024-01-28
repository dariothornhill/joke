{
  description = "Python API Development Shell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable-small";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }: {
    devShell = {
      buildInputs = [
        nixpkgs.python38
        poetry2nix
      ];
      shellHook = ''
        export PYTHONPATH="${self}";
      '';
    };
  };
}

