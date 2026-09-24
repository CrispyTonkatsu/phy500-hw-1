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
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          libGL
          glfw

          julia
          gfortran.cc.lib
          stdenv.cc.cc.lib
        ];

        LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
          pkgs.libGL
          pkgs.glfw

          pkgs.gfortran.cc.lib
          pkgs.stdenv.cc.cc.lib
        ];
      };
    };
}
