with import <nixpkgs> {};
#{pkgs, stdenv, buildEnv, ...}:

stdenv.mkDerivation {
  name = "ffs-api";

  src = ./.;
  
  buildInputs = with pkgs; [
    python35
  ];

  PYTHONIOENCODING = "utf8";

  installPhase = ''
    ${pkgs.python35}/bin/python3.5 genapi.py nodes.json
    mkdir $out/
    cp -r v0 $out/
  '';

  fixupPhase = "true";
}
