# Flatpak remote

Personal Flatpak remote for applications I distribute through Flatpak. One
remote, many apps: add it once, then install any of them — updates arrive
through `flatpak update`.

## Install

```sh
flatpak remote-add borisovodov https://borisovodov.github.io/flatpak/borisovodov.flatpakrepo --user
flatpak install borisovodov doru
```

The repository is signed with a dedicated GPG key (embedded in the
`.flatpakrepo` file), so every update is verified against it. Both
x86_64 and aarch64 builds are published. The `.flatpakrepo` file also
declares Flathub as the runtime repository (`RuntimeRepo=`), so adding
this remote offers to add Flathub — the runtime and the Electron base
app come from there.

## Apps

| App | ID |
|---|---|
| [Dóru](https://doru.family) — local-first genealogy for the AI era | `org.doru.doru` |

## How it works

The `build.yml` workflow watches the Dóru releases every four hours. When a
new release appears, it checks out the tag, builds the flatpak on an Ubuntu
runner (electron-builder with the `org.electronjs.Electron2.BaseApp`
base, runtime 25.08), imports the bundle into an OSTree repository, signs
it with the GPG key (secret `FLATPAK_GPG_KEY`), smoke-installs it from the
built repository, and publishes it to the `pages` branch — served by GitHub
Pages at the URL above.

The remote is served from GitHub Pages. This is the publisher-level
repository, so the URL is `borisovodov.github.io` — a per-app custom domain
would not fit the one-remote-many-apps model.

## Adding another app

Create an `org.example.app/` directory with a `version.txt` marker (set to
`none` initially) and add a job to `.github/workflows/build.yml` that
builds it the same way — one OSTree repository serves any number of apps.
