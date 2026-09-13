---
title: "The definitive guide to Durable Execution"
details: "Tom Wheeler's May 2025 Temporal blog post defining Durable Execution as crash-proof execution, naming its four universal characteristics (virtualized execution, time-independence, automatic state preservation, hardware agnosticism), and arguing it elevates development by letting developers write code for the goal rather than for every failure mode."
tags:
  - raw
  - blog-post
  - durable-execution
  - runtime
source: https://temporal.io/blog/what-is-durable-execution
created: 2026-09-10
updated: 2026-09-10
type: raw
authors:
  - Tom Wheeler
published: 2026-05-06
---

# The definitive guide to Durable Execution

**Source:** https://temporal.io/blog/what-is-durable-execution
**Author:** Tom Wheeler
**Published:** 2026-05-06
**Category:** Temporal Concepts

---

When I joined Temporal three years ago, hardly anyone I met at conferences had heard of us. Explaining what we did was challenging because there wasn't much they could compare it to. People often learn new things by connecting them to what they already know. Someone familiar with PostgreSQL, for example, will quickly understand the role of some other relational database, such as IBM DB2 or Microsoft SQL Server.

It felt a bit like trying to describe an iPhone to someone from 1975. You could say it's both a phone and a camera, but that doesn't really capture how transformative it is. These days, everyone knows what a smartphone is — no explanation needed.

Temporal is typically categorized as a Durable Execution Platform, but this often raises the question, "What is Durable Execution?" I've heard many definitions, both inside and outside the company, and given several myself. Most are either overly complex or blur the line between what Durable Execution is and how it's implemented or supported by various platforms.

After thinking about this for months, I delivered a talk at our Replay '25 conference in London. This blog post summarizes the key points from my talk, starting with a clear definition of Durable Execution and continuing with why it fundamentally changes how developers build reliable applications.

## What is Durable Execution?

**Durable Execution is crash-proof execution.**

It enables developers to write reliable software with less effort. It lets them focus on what the application should achieve instead of anticipating and trying to handle everything that might go wrong along the way.

## Why is Durable Execution important?

Developers spend significant time writing code to detect and handle failures. In fact, computer science Professor Flaviu Cristian observed in *Reliable Computer Systems* that this type of code often accounts for more than two-thirds of all code in a production system — far more than what's dedicated to the "happy path" where no failures occur.

The world has changed since that book was published. Cloud computing, microservices, and event-driven architectures have transformed software development. Modern applications are distributed systems, with many more potential points of failure, yet the expectations of reliability have never been higher.

> Failures are inevitable.
> Durable Execution makes them inconsequential.

Durable Execution offers three key benefits:

1. It improves application reliability by providing fault tolerance.
2. It simplifies code by allowing it to focus on the goal instead of potential problems.
3. It accelerates development by eliminating the need to write complex error-handling logic.

## What is a Durable Execution platform?

Durable Execution is made possible by an abstraction that insulates code from crashes and enables applications to continue running despite them. A Durable Execution platform is the system that provides this abstraction.

Most Durable Execution platforms refer to the abstraction as a workflow, although this term is not universal. Adding to the confusion, relatively few of the systems typically referred to as "workflow engines" actually provide Durable Execution.

Although the terminology may vary from one Durable Execution platform to the next, what they all have in common is the ability to deliver crash-proof execution.

## Four key characteristics of Durable Execution

There are important differences between Durable Execution platforms, including how they work and the additional capabilities they offer. However, the concept of Durable Execution and what it means for developers is universal. The four key characteristics that follow apply to all Durable Execution platforms.

### 1. Durable Execution virtualizes execution

To describe Durable Execution as crash-proof does not suggest that a crash cannot happen. It means that a crash will have no consequence. To make an analogy, wearing a waterproof watch doesn't prevent you from falling into a swimming pool. Instead, it guarantees that the watch will continue running despite it.

Execution normally takes place within a single process, running on a single machine, and will immediately end if that process crashes for any reason. Why might an application crash? There are countless reasons. It could result from a bug in the application code, a bug in a library used by that code, a bug in the operating system, a power outage, or a hardware failure. Regardless of the cause, the outcome is the same. The values of the variables updated while the application was running are lost, along with the notion of which statements already ran and which one should run next.

Durable Execution is crash-proof because it virtualizes execution, enabling it to take place across a series of processes, each of which can potentially run on a different machine than the one before. If the current process happens to crash, Durable Execution ensures that work transparently resumes in a new process. The application state is recreated in that new process, after which execution will continue as if the failure never happened at all.

An example will help to illustrate this concept. Consider an application that requires five steps to achieve its goal. Let's say that it successfully completes steps A and B, but crashes before completing step C. Without Durable Execution, execution would come to an end, and there would be no further progress.

With Durable Execution, however, the work resumes in a subsequent process. Since the state is fully reconstructed in this new process, all variables have the same values as they did at the time of the crash, including the results from the previously completed steps.

Let's say that step C now completes, but a hardware failure causes this second process to terminate during step D. Once again, the execution will resume in a subsequent process — this time on a new machine — and will continue making progress until the application achieves its goal.

In this case, execution happened to span three different processes across two different machines. Practically speaking, these details don't matter because this is how it looks from the developer's perspective.

### 2. Durable Execution is not limited by time

Because Durable Execution enables applications to withstand crashes, it enables them to run for as long as needed to reach their goal. An execution that processes a payment may complete in a fraction of a second, but one that manages a loan may need to run for several years.

Some applications naturally involve long periods of inactivity. For example, an application for customer onboarding might need to send emails at certain intervals during the first year. Without Durable Execution, you might implement this with a scheduler system and an application database, since you can't expect a program started today to still be running six months from now. That complexity isn't necessary with Durable Execution, since you can reliably achieve the same result with nothing more than a for-loop and a sleep statement. The example below illustrates this, using pseudocode to avoid the implementation details of a specific platform or programming language:

```
function Notifier(String username) {
    // notify customer at each defined interval
    for interval in [1, 7, 30, 60, 90, 180] {
        sleep(Time.days(interval))
        sendNotification(username)
    }
}
```

The `sleep` call in the example above illustrates another important point. Durable Execution enables an individual API call to await a result for as long as necessary, regardless of whether that takes a few seconds or several months.

### 3. Durable Execution automatically preserves application state

Without the benefit of Durable Execution, a crash causes the values of variables within the running application to suddenly disappear, resulting in the loss of its state.

One way to guard against this is to use an application database, since it provides a place for those values to live when the application that generated them stops running. Developers who employ this approach must write tedious code to copy values from the application and store them into the database, only to later load them from the database and update the variables within the application. In such cases, using a database isn't the actual goal — it might not be mentioned in the requirements at all — it's just a defensive mechanism intended to protect the application from a crash.

With Durable Execution, you don't need an application database nor all the code necessary to interact with it to guard against a crash. Durable Execution is crash-proof execution, which means that all of the variables in your application, including local variables, are durable. They will have the same values after a crash as they did before it.

There are often good reasons to use an application database, even with Durable Execution. You might use one for reporting purposes, for example, but you won't need one to protect your application from a crash.

### 4. Durable Execution is hardware agnostic

For many years, reliable systems emphasized fault tolerance through hardware, in some cases favoring very expensive machines with exotic features such as hot-swappable CPUs and memory. This makes sense for certain applications where the cost of downtime is exceptionally high. Fault-tolerant hardware may reduce the likelihood of failure, but it can never eliminate it. Consequently, these systems cannot guarantee that execution will continue if that failure does occur. Furthermore, hardware-based fault tolerance offers no protection against crashes caused by software defects, such as a divide-by-zero error in the application or a kernel panic in the underlying operating system.

Conversely, Durable Execution builds reliability into the software. While Durable Execution platforms vary in terms of system requirements, Durable Execution itself does not depend on any specific hardware. In fact, applications that use Durable Execution can be deployed to virtual machines or containers. Unlike hardware-based solutions for fault tolerance, Durable Execution is not bound by physical proximity, does not require specialized networking equipment, and works natively in both local data centers and cloud environments.

Through its ability to span multiple processes and systems over time, Durable Execution can overcome crashes, regardless of whether they result from software failure or hardware failure. This is welcome news for any developer tasked with designing and building mission-critical applications.

## Durable Execution elevates development

Platforms provide powerful abstractions that decouple how we view the system from how it exists in reality. For example, the filesystem abstraction provided by UNIX allows us to think about storage in terms of files instead of sectors on a disk. Databases build on this to further elevate our thinking. By delegating to the database, developers gain the ability to think in terms of fields, records, and tables instead of being concerned with file structures and serialization formats.

Durable Execution similarly elevates application development. Think about all of the complexity involved with mitigating failures, from implementing retry and timeout logic, to manually loading and saving application state, and even using external schedulers to overcome the practical limits of time. Now, imagine how much simpler your application would be if it just couldn't fail. What you're imagining is Durable Execution.

In addition to making the application more resilient, Durable Execution makes developers more productive by liberating them from the burden of writing, testing, and maintaining all of the code described above.

## In conclusion

By increasing application reliability, reducing code complexity, and boosting developer productivity, Durable Execution offers significant value to application developers.

While the platforms that provide Durable Execution vary according to their capabilities, advantages, and limitations, all of them enable a fundamental change in how developers build and run modern production applications.
