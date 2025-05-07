import { serve } from "bun";

serve({
  port: 3000,
  fetch(req) {
    return new Response("Hello from Bun Server!", { status: 200 });
  },
});
