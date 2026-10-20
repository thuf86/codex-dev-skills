---
name: android-apk
description: Use for Android Kotlin, Jetpack Compose, XML layouts, Gradle builds and APK UI changes.
---

# android-apk

## Activation
Use for Android projects, Gradle, Kotlin, Compose, XML layouts, navigation, session persistence or APK packaging.
## Workflow
1. Inspect AndroidManifest, module build files, navigation, UI state and authentication boundaries.
2. Establish baseline build and identify target SDK, minimum SDK and signing constraints.
3. Apply minimal UI changes consistent with Material design and accessibility.
4. Preserve package identifiers, backend endpoints, authentication contracts, permissions and storage semantics unless explicitly authorized.
5. Run relevant Gradle assemble/test/lint tasks when the toolchain exists; verify generated APK path and signing type.
## Guardrails
Never embed API secrets or passwords in source. Do not bypass licensing, platform security or access controls. Do not report an APK as produced unless it exists and is verified.
## Deliverable
List modules/files, build commands, test outcomes, APK path if produced, and unresolved constraints.
