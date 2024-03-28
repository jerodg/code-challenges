<script>
  import { formatRelative } from 'date-fns';

  let promise = fetch(
    `${document.location.origin}/api${document.location.pathname}`,
  )
  .then(response => response.json());

  function reply({ text, tweet_id, username }) {
    window.alert(`
      text: ${text}
      tweet id: ${tweet_id}
      username: ${username}
    `);
  }
</script>

<main class="container mx-auto mt-12 h-screen">
  {#await promise}
    Loading tweets...
  {:then response}
    <section class="flex flex-col">
      {#each response.tweets as t}
        <article class="flex items-start mb-4 hover:bg-grey-100">
          <img
            src={t.profile_image_url}
            alt="profile"
            class="w-10 h-10 rounded mr-3"
          >
          <div class="flex flex-col">
            <div class="flex items-end">
              <span class="font-bold text-md mr-2 font-sans">
                @{t.username}
              </span>
              <span class="text-grey text-xs font-light">
                {formatRelative((1000 * t.timestamp), Date.now())}
              </span>
            </div>
            <p class="font-light text-md text-grey-darkest pt-1">
              {t.text}
            </p>
            <button
              type="button"
              class="bg-blue-500 hover:bg-blue-700 h-5 w-8 my-auto rounded-full"
              on:click={() => reply(t)}
            >
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65 72" class="mx-auto w-4">
                <path d="M41 31h-9V19c0-1.14-.647-2.183-1.668-2.688-1.022-.507-2.243-.39-3.15.302l-21 16C5.438 33.18 5 34.064 5 35s.437 1.82 1.182 2.387l21 16c.533.405 1.174.613 1.82.613.453 0 .908-.103 1.33-.312C31.354 53.183 32 52.14 32 51V39h9c5.514 0 10 4.486 10 10 0 2.21 1.79 4 4 4s4-1.79 4-4c0-9.925-8.075-18-18-18z" fill="white"/>
              </svg>
            </button>
          </div>
        </article>
      {/each}
    </section>
  {:catch error}
    {error}
  {/await}
</main>

<style>
</style>
