<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 0c28d1c23a1bb2a3357562cb26ba979fad9c174825726241f913eb7e11e7af18 -->

# Astry website

Static Astro landing page for Astry. Source lives in `app/`.

Install [mise](https://mise.jdx.dev/) and check out [nicodes/tools at the reviewed revision](https://github.com/nicodes/tools/tree/1b0fc8e6c9a1e4284bcc32c0011ecdc0cd3843b7) into `.ci-tools`. Run `mise install`, then `mise run dev`. The local site opens at `http://127.0.0.1:4321`. `mise run stop` stops this checkout's session.

Run `mise run check` for type checks, the production build, metadata and accessibility assertions, artwork checks, performance budgets and dependency auditing. `mise run clean` removes generated site output.

For Vercel, import this repository with the repository root as the Root Directory. The committed `vercel.json` selects the install/build commands, publishes `app/dist`, and preserves the site's security headers. No environment variables are required. The canonical site URL remains `https://info.astry.app`; attach that domain when configuring Vercel.
