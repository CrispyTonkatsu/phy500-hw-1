{
  description = "Julia environment for hw1";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs, ... }:
    {
      devShells = builtins.mapAttrs (
        system: pkgs:
        let
          pythonEnv = (
            pkgs.python3.withPackages (
              ps: with ps; [
                plotly
                numpy
                scipy
                sympy
              ]
            )
          );
        in
        {
          default = pkgs.mkShell {
            buildInputs = with pkgs; [
              basedpyright
              ruff

              pythonEnv
            ];
          };
        }
      ) nixpkgs.legacyPackages;
    };
}
