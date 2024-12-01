# save this as shell.nix
{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
 buildInputs = [
   pkgs.rustc
   pkgs.cargo
 ];
 packages = [ ];
 hardeningDisable = [ "all" ];

}
