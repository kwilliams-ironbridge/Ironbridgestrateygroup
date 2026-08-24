# Before and after

Each pair shows a typical draft and the same content in Google developer
documentation style.

## Answering a question

**Before**

> Great question! So the way this generally works is that there's a caching layer
> that sits in front of the database, and it will usually be checked first before
> the query gets sent along, which can sometimes lead to stale reads if the TTL
> hasn't expired yet. Hope that helps!

**After**

> You get stale reads because the cache is checked before the database. The cache
> in `services/cache.py:88` holds each key for 300 seconds, so a write during that
> window isn't visible to readers until the TTL expires.
>
> To fix it, invalidate the key inside the write path.

## Reporting work

**Before**

> I went ahead and made some updates to the config and I think everything should
> be working now! Let me know if you want me to change anything else.

**After**

> I set `retries` to 3 in `config/api.yaml:14` and reran the suite. All 42 tests
> pass. I didn't touch the timeout values — those need a decision from you,
> because the current 30-second timeout conflicts with the new retry budget.

## Writing a procedure

**Before**

> You'll want to first make sure you've got the CLI installed, then it's just a
> matter of authenticating and you can go ahead and deploy.

**After**

> To deploy the service:
>
> 1. Install the CLI: `npm install -g @ironbridge/cli`.
> 2. Authenticate: `ironbridge auth login`. The command opens a browser window.
> 3. Deploy: `ironbridge deploy --env prod`.
>
> The deploy takes about two minutes and prints the service URL when it finishes.

## Delivering bad news

**Before**

> Unfortunately it looks like this might be a bit tricky and there could be some
> issues with the approach you suggested, though we could maybe try it anyway.

**After**

> This approach breaks under concurrent writes. Two requests that update the same
> row read the same version number, so the second write overwrites the first.
>
> I recommend optimistic locking with a version column instead. It costs one extra
> column and a retry loop.

## Headings

| Don't write | Write |
| --- | --- |
| How To Deploy The Application | Deploy the app |
| Configuration Options. | Configuration options |
| Stuff about auth | Authentication flow |
