import { Hono } from 'hono'
import { sign, verify, decode } from 'hono/jwt'
import { PrismaClient } from '@prisma/client/edge'
import { withAccelerate } from '@prisma/extension-accelerate'

const app = new Hono<{
	Bindings: {
		DATABASE_URL: string
	}
}>()

app.get('/api/contest/:page?', async (c) => {
  const page : number = Number(c.req.param('page')) || 1
  
  const prisma = new PrismaClient({
		datasourceUrl: c.env?.DATABASE_URL,
	}).$extends(withAccelerate())

  const contests = await prisma.contest.findMany({
    orderBy: {
      start_time: 'desc',
    },
    include: {
      problems: true
    },
    skip: (page - 1) * 10,
    take: 10,
  })

  return c.json({ contests })
})

export default app
