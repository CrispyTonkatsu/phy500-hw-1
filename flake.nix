{
  description = "Julia environment for hw1";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      pythonEnv = (
        pkgs.python3.withPackages (
          ps: with ps; [
            plotly
            numpy
            sympy
          ]
        )
      );
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          basedpyright
          ruff

          pythonEnv
        ];
      };
    };
}
