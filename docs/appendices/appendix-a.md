(appendix-a)=

# Appendix A. Laboratory and Project Guide

(appendix-a-a-1-choose-a-laboratory-by-its-learning-objective)=

## A.1 Choose a laboratory by its learning objective

The companion directory separates applications that illustrate different mechanisms. Run commands from the named laboratory directory rather than from the book root. Each laboratory has its own README, dependencies, input data, and result provenance. They are not one production system, and completing one does not validate every capability described in the book.

```{list-table}
:header-rows: 1
:class: book-table

 * - **Chapters**
   - **Directory under Labs/**
   - **Starting point**
 * - 2
   - foundation/
   - Synthetic observation walkthrough and deterministic summary foundation
 * - 4
   - digital\_twins/
   - Local observation replay, entity state, freshness, and a teaching prediction model
 * - 5–9
   - foundation/systems/
   - Callable analysis service, client, journal, policies, and deployment descriptions
 * - 10
   - edge\_ai/
   - Supplied digit-classifier artifacts, inference, compression and optional training
 * - 11
   - collaborative\_ai/
   - Classifier cascades, same-model splitting, and a local-model API adapter
 * - 12
   - edge\_agents/
   - Authorized queries, lexical retrieval, restricted expressions, budgets and recovery
 * - 13–14
   - trust\_and\_ledgers/
   - Signed records, policy checks, history validation and a single-process registry
```

Use institution-approved environments and synthetic or explicitly permitted data. An educational HTTP endpoint is not an authenticated service for public deployment. Do not expose model or development services to an untrusted network merely to make a demonstration easier.

(appendix-a-a-2-observation-and-deployment-foundations)=

## A.2 Observation and deployment foundations

The original roomedge.py foundation accepts records, identifies duplicates, stores local history, constructs bounded evidence, and presents deterministic facts or a replaceable summary. Its stub mode is not a language model. It assumes a trusted local caller and does not implement user authentication, model-directed planning, arbitrary code execution, or a complete agent. {ref}`Chapter 2 <chapter-2>`’s prepared task walkthrough is a separate synthetic fixture, not a transcript of real model planning.

From Labs/foundation/, start with the local demo and tests documented in its README. From Labs/foundation/systems/, run the small service and client, compare worker/version identifiers, and inspect the persisted event journal. Keep a record of request inputs and returned values before comparing time. The deployment generators create inspectable container, cluster, and Greengrass descriptions; generating a description does not prove that a target cluster or cloud device accepted it.

Commercial-platform work needs an approved account, narrowly scoped credentials, an identified deployment target, compatible artifacts, and a cost boundary. Recheck the dated platform documentation before the laboratory. Do not substitute broad administrator privileges for understanding a permission failure.

(appendix-a-a-3-digital-twins-retain-observation-meaning)=

## A.3 Digital twins: retain observation meaning

The digital-twin replay maps observations to identified entities, retains late history without replacing newer state, detects conflicting duplicate events, and reports stale information. The scenario model is deliberately simple and uses declared assumptions. Store its predicted trajectory separately from observed state. A rendered scene or a predicted value is not evidence of a new physical measurement.

Change arrival order, duplicate one event, and advance the query time while holding observations fixed. Predict the state and freshness result before running the program. Then alter the hypothetical model coefficient and explain why this changes a scenario rather than the recorded history.

(appendix-a-a-4-edge-ai-infer-first-then-compare-changes)=

## A.4 Edge AI: infer first, then compare changes

Begin with the supplied small digit models and saved inputs. The NumPy path reads the laboratory’s documented dense/ReLU parameter arrays; it is not a general interpreter for arbitrary downloaded model files. The optional PyTorch path reproduces training, dynamic-INT8 execution, pruning, and direct-versus-distilled student comparisons using the recorded environment.

The data are cropped 8 × 8 digit images, not a complete camera reader. The three initializations share one sample split; they do not establish variation across writers or field deployments. Keep the weaker distillation result recorded in Chapter 10. A valid experiment need not make an advertised method win. Choose new settings using development/validation data, and name any reused evaluation set rather than describing it as new independent evidence.

Record cold loading separately from warm inference, and model-call time separately from sensor acquisition and application latency. Run a new study into a new directory; never overwrite the supplied measured record while attempting reproduction. Target-board execution, energy, peak memory, static PTQ/QAT, and accelerator performance require separate experiments.

(appendix-a-a-5-collaboration-preserve-the-comparison-boundary)=

## A.5 Collaboration: preserve the comparison boundary

The collaboration experiment reuses {ref}`Chapter 10 <chapter-10>` artifacts without retraining. Select the cascade rule on validation inputs and report rescued and damaged predictions as well as total accuracy. The recorded cascade did not improve the local classifier in this setup. The result concerns these models and this inherited sample set, not the general value of collaboration or language models.

Same-model partition tests serialize and reconstruct intermediate values on one CPU host. They establish numerical behavior across that software boundary, not a real network speedup. The optional local language-model adapter can connect to an installed endpoint; interface tests use an explicit HTTP test double. They do not establish actual model quality, memory use, or latency.

(appendix-a-a-6-agents-distinguish-proposal-execution-and-evidence)=

## A.6 Agents: distinguish proposal, execution and evidence

The {ref}`Chapter 12 <chapter-12>` runtime executes local data queries, lexical document retrieval, restricted analysis expressions, result checks, and SQLite task recovery. Its default planner is scripted. The optional model adapter is a separate path that must be evaluated with the selected model and tasks. Neither a script nor an HTTP test double should be labeled model reasoning.

A proposed tool call is not yet an executed action; a stored result identifier does not prove that every sentence citing it is correct. Retain the negative control in which a correct computed 27.25 °C result is accompanied by false 99 °C prose. The narrow format/provenance checks accept the reference, while the independent numeric task check detects the false claim.

Restricted expressions are not a production sandbox for arbitrary Python. A future general-code runner needs a separate isolation design, resource limits, denied-by-default network and file access, and target-environment testing. Task recovery here reopens a local database under one controller; it does not demonstrate exactly-once remote effects or recovery from every physical power-loss scenario.

(appendix-a-a-7-trust-test-what-each-mechanism-actually-establishes)=

## A.7 Trust: test what each mechanism actually establishes

The trust laboratory performs local signature and hash operations, checks access/update conditions, saves records, and reopens a single-process registry. It also records simulated action approval without operating equipment. Use freshly generated local demonstration keys; keep private keys out of reports and shared packages.

Four negative controls matter: a valid signer can submit a false measurement; an authentic old history can pass a local check without a newer trusted checkpoint; two individually valid signed forks do not constitute consensus; and a fresh cached status can miss a newer remote revocation. Explain these cases before proposing a ledger or an automated actuator.

A static signature-threshold checker is not a distributed consensus implementation. The lab does not deploy DCL, Fabric, smart contracts, hardware attestation, or a live identity infrastructure. Platform examples in {ref}`Chapter 14 <chapter-14>` describe documented architectures; consult their versioned sources and validate a real deployment separately.

(appendix-a-a-8-a-course-project-beyond-the-examples)=

## A.8 A course project beyond the examples

Choose an application with an explicit user, input source, useful output, and reason to consider edge execution. The project may use perception, language, ordinary analytics, or a combination. It need not use a language model or a blockchain merely because these appear in the book.

Establish a baseline before optimizing. State the supported tasks and the quality requirement, then record deployment location, latency, resource use, communication, and at least one failure mode. Compare one meaningful alternative while preserving input and acceptance conditions. A claimed improvement should name its mechanism, its cost, and the condition under which it stops helping.

A proposed assessment allocates 25% to task definition and a working baseline, 25% to the architecture and implementation, 30% to controlled evaluation, and 20% to reproducibility, limitations, and presentation. Treat this as a transparent assessment proposal rather than a claim that every institution uses the same rubric. The final submission should include a short architecture diagram, execution instructions, source/configuration identifiers, allowed data, results, and a known-limitations statement.

