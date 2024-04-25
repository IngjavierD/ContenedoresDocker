FROM rust:1.69-slim as builder

WORKDIR /app

COPY Cargo.toml ./
RUN mkdir src && echo "fn main() {}" > src/main.rs

RUN cargo build --release

COPY . .
RUN touch src/main.rs && cargo build --release

FROM debian:buster-slim

RUN apt-get update && apt-get install -y libssl1.1 ca-certificates

COPY --from=builder /app/target/release/hello-rust /app/hello-rust

EXPOSE 8080

CMD ["/app/hello-rust"]