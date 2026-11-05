(appendix-d)=

# Appendix D. Glossary and Notation

(appendix-d-d-1-core-vocabulary)=

## D.1 Core vocabulary

**Admission control.** A decision about whether to accept additional work given resource, policy, or deadline constraints. It prevents overload from becoming an uncontrolled failure.

**Agentic workflow.** A workflow in which a model chooses some actions or next steps. Its executor still needs independent authorization, state, and budget controls.

**Application invariant.** A property that must remain true across valid executions, such as never counting one logical observation twice.

**Artifact.** A deployable file or package, such as executable code, configuration, or model weights. Artifact identity and mutability affect reproducibility.

**Availability.** Ability to obtain service under a specified request and failure model. It is not interchangeable with freshness, correctness, or an uptime percentage measured at a different boundary.

**Backpressure.** A mechanism that limits upstream production or admission when downstream capacity is constrained.

**Cache.** A retained result or data copy used to avoid repeated work. Correct use requires an identity and validity rule.

**Cascade.** A policy that attempts one model or service, evaluates the result, and conditionally invokes another.

**Cold start.** Initialization work before a request can execute on a previously inactive instance or unloaded runtime.

**Consensus.** Agreement on decisions among participants under a specified failure model. It is not merely several models producing similar text.

**Consistency.** Rules describing which values distributed reads and writes may observe. The term must be qualified by the intended model.

**Container.** An execution and packaging abstraction using operating-system isolation mechanisms. It does not eliminate host-kernel, hardware, or resource dependencies.

**Control plane.** Mechanisms for configuring, deploying, coordinating, and managing a system. Its communication can be separate from application-data traffic.

**Critical path.** The longest dependency path in a task graph under assigned durations. It limits completion time even when other tasks can run in parallel.

**Data plane.** Paths and mechanisms that carry or process the application’s working data.

**Deadline.** The time by which an operation is required or intended to finish. Stopping the caller’s wait does not automatically cancel remote execution.

**Deployment.** Installing or selecting artifacts and configuration on an execution target. Accepted deployment requests and successful application behavior are different observations.

**Digital twin.** A model associated with a physical entity and updated according to a defined relationship. Its usefulness depends on fidelity, synchronization, and purpose, not the label alone.

**Edge–cloud continuum.** A coordinated set of resources across devices, nearby infrastructure, and cloud locations. It is not necessarily a single owner or one flat execution environment.

**Event time.** The producer’s time associated with an observation or event, distinct from its receipt and processing times.

**Fencing token.** A version or authority marker that a resource checks to reject operations from a superseded owner.

**Freshness.** How current information is relative to the time and semantics of a query. High message throughput does not guarantee fresh user-visible state.

**Idempotency.** A property under which repeating an operation has no additional relevant effect beyond performing it once, according to the operation’s contract.

**Inference.** Using a trained model to produce an output for an input. It is distinct from updating the model through training.

**Jitter.** Variation in timing, or intentional randomized delay used to avoid synchronized retries. State which meaning is intended.

**Lease.** Time-bounded authority or ownership under specified clock and communication assumptions.

**Logical event identifier.** A stable identifier for the event itself, preserved across delivery attempts.

**Offloading.** Moving work to another execution location. Its value depends on communication, execution, state, policy, and resource conditions.

**Orchestration.** Coordinating deployment and execution across components and resources, including desired state and lifecycle management.

**Outbox.** A durable record of work to send, committed with related local state so a failure cannot silently separate the two.

**Placement.** Assigning computation or state to a location. Dynamic changes may require migration and warm-up.

**Prefill and decoding.** Input-context processing and incremental output generation in a language-model serving path. Their resource behavior may differ.

**Provenance.** Information about the origin and transformations of data or results, used to trace how a claim was produced.

**Quorum.** A required set or number of participants whose responses permit an operation under a coordination protocol.

**Replication.** Maintaining copies of state or service across locations. It requires explicit update and failure semantics.

**Retained message.** A broker-stored topic value available to later subscribers under a messaging protocol. It is not inherently a new physical observation.

**Routing.** Selecting an execution path or model for a request. In this book, distinguish request routing from network packet routing.

**Safety.** Avoidance of unacceptable harm under the application’s operating and failure conditions. It is not established by model confidence or network security alone.

**Service-level objective.** A chosen target for a defined service indicator over a stated population and interval. The target must name the measured boundary.

**Snapshot.** An evidence set or state view associated with defined selection and consistency semantics.

**Speculative decoding.** Drafting and verifying tokens to accelerate a target model under a specified algorithm. Correct acceptance and correction rules matter.

**Stateful service.** A service whose relevant behavior depends on information retained across requests or executions.

**Tail latency.** The slower portion of a response-time distribution, often described by high percentiles with a defined sample population.

**Trust boundary.** A boundary across which assumptions about identity, authority, or data reliability change.

**Zero trust.** An approach that does not grant implicit trust merely from network location or ownership; access is evaluated using explicit policy and context. [{ref}`25 <ref-25>`]

(appendix-d-d-2-units-and-recurring-notation)=

## D.2 Units and recurring notation

Use decimal units for network rates unless stated otherwise: 1 MB is $10^{6}$ bytes and 1 Mb is $10^{6}$ bits. Use binary units when discussing binary memory capacities: 1 MiB is $2^{20}$ bytes and 1 GiB is $2^{30}$ bytes. One byte is eight bits. Converting a byte payload using a bit-rate link without that factor creates an eightfold error.

```{list-table}
:header-rows: 1
:class: book-table

 * - **Symbol**
   - **Meaning in this book**
   - **Typical unit**
 * - $D$ or $S$
   - Data size, with local definition
   - bytes or MB
 * - $B$
   - Effective throughput, not just nominal link rate
   - bytes/s or MB/s
 * - $T$
   - Duration, or token count when explicitly defined
   - seconds or tokens
 * - $\lambda$
   - Request arrival rate in a queue model
   - requests/s
 * - $\mu$
   - Service rate in a queue model
   - requests/s
 * - $\rho$
   - Utilization ratio $\lambda/\mu$ in the teaching model
   - dimensionless
 * - $C$
   - Cost under a declared accounting boundary
   - currency or toy cost units
 * - $E$
   - Energy
   - joules or watt-hours
 * - $P$
   - Power, or probability when explicitly defined
   - watts or dimensionless
 * - $M$
   - Memory or storage quantity
   - bytes, MiB, or GiB
```

Symbols are local to an equation unless a section states otherwise. In particular, the $T$ in the cache estimate is token count, not elapsed time. A formula is useful only when its units and assumptions are explicit.

(appendix-d-d-3-additional-device-networking-and-stream-processing-terms)=

## D.3 Additional device, networking, and stream-processing terms

**ADC.** Converts an analog signal into discrete numerical samples. Resolution does not by itself establish measurement accuracy.

**IMU.** A combination of inertial sensors, typically accelerometers and gyroscopes. Orientation and position estimates require additional assumptions and processing.

**GATT.** The Bluetooth attribute-oriented procedure framework for discovering and interacting with services and characteristics. Application semantics remain necessary.

**6LoWPAN.** An IPv6 adaptation approach for constrained links, including header compression and fragmentation mechanisms defined by its specifications.

**LoRa / LoRaWAN.** LoRa is a radio modulation technology; LoRaWAN specifies a network architecture and protocol behavior built around compatible radio links.

**DDS.** Data-centric publish–subscribe middleware with typed topics and configurable quality-of-service policies; it is not a physical radio.

**Event time / processing time.** Event time represents when an event is said to have occurred; processing time represents when a processing system handles it. Clock meaning must be defined.

**Watermark.** A progress statement used in stream processing to reason about event-time completeness under declared lateness assumptions; not a guarantee that no late event exists.

**RTOS.** An operating-system design supporting scheduling and timing-oriented services. Deadline satisfaction still requires workload and platform analysis.

**Proprioceptive / exteroceptive sensing.** Sensing of a platform’s own state versus its surrounding environment; both can contribute to a robot or vehicle state estimate.

**Attestation.** Evidence about a platform or software state evaluated by a verifier against a policy. Freshness, identity, and the measurement boundary are part of the claim.

**Age of information.** At an observation time, elapsed time since generation of the newest useful update. It differs from the latency of one successfully delivered packet.

(appendix-d-d-4-agentic-application-vocabulary)=

## D.4 Agentic application vocabulary

**Agentic application.** An application in which a model helps choose or revise tasks and tool calls in response to a goal and returned observations. The surrounding software still controls execution and permissions.

**Data catalog.** Descriptions of available sources, fields, units, intervals, and quality that help determine what can be queried. A catalog description is not the observation history itself.

**Task plan.** An inspectable statement of intended operations and their dependencies. It is neither evidence that those operations ran nor a record of a model’s hidden reasoning.

**Analysis artifact.** A data extract, program, table, plot, or report produced during a request. Identifiers help trace artifacts to inputs and execution; they do not grant access.

**Answer oracle.** An independently established expected result or evaluation rule used to check a task outcome. A deterministic oracle is not a substitute for the model behavior being evaluated.

(appendix-d-d-5-ai-digital-twin-and-trust-terminology)=

## D.5 AI, digital-twin and trust terminology

**Activation.** An intermediate value produced while evaluating a model; unlike a weight, it depends on the current input.

**Calibration.** Estimating a representation range or checking a predictive score against observed outcomes; specify which meaning is intended.

**Distillation.** Training a student using information supplied by a teacher; it is not merely compressing a file, and the teacher need not run during student inference.

**Pruning.** Removing or masking selected model parameters or structures; execution savings depend on representation and supported kernels.

**Quantization.** Mapping numerical values into a lower-precision representation with specified scale, range and rounding behavior.

**Post-training quantization.** Converting an already trained model, sometimes using representative calibration data, without the full quantization-aware training procedure.

**Quantization-aware training.** A training procedure that models relevant quantization effects so learned parameters can adapt to the intended representation.

**Early exit.** Producing an output from an intermediate model branch when an evaluated exit rule accepts it, rather than always using the full network.

**Prefill.** Processing input context to prepare the state used in subsequent autoregressive generation.

**KV cache.** Retained attention key/value states that can avoid recomputing preceding context; its size depends on architecture and active sequences.

**Retrieval-augmented generation.** Using retrieved external evidence in a model request; retrieval does not by itself establish relevance, permission or factual correctness.

**Federated learning.** Coordinating model learning from locally held data through exchanged updates; distinct from collaborating on one inference request.

**Digital-twin prediction.** A scenario or estimated future state produced by a behavior model; store its assumptions and provenance separately from observations.

**Remote attestation.** Evidence about a platform or software state, appraised against a policy; not a universal proof of correct future behavior.

**Signed manifest.** A protected description of an artifact, its target and permitted update conditions.

**Revocation.** Withdrawal of a previously granted status or permission; a disconnected cache may not learn it immediately.

**Trusted checkpoint.** An independently trusted history commitment used to detect some rollback or inconsistency that local self-consistency alone cannot reveal.

**Permissioned ledger.** A shared-record system in which defined authorities govern who may participate in specified writing, validation or administration roles.

**On-chain / off-chain.** Distinguishing records maintained through the ledger mechanism from data or operations handled outside it; their linkage still needs design.

**Smart contract.** Programmed rules for state transitions within a specified platform; correct execution does not validate the truth of external inputs.

**Data provenance.** Information about where a record came from and how it was transformed; it supports tracing but does not certify physical truth.

