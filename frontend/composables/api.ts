export async function useApi(baseUrl: string, method: 'POST' | 'DELETE' | 'PUT' | 'PATCH', body?: object) {
    const toast = useToast()
    const successMessages: Record<string, string> = {
      POST: 'Successfully added',
      DELETE: 'Successfully deleted',
      PUT: 'Successfully updated',
      PATCH: 'Sucessfully updated',
    }

    try {
      const res = await $fetch(baseUrl, {
        method,
        body,
      })
      toast.add({
        title: 'Success',
        description: successMessages[method],
      })
      return res
    }
    catch (err: any) {
      toast.add({
        title: 'Error',
        description: err.data.statusMessage || err.data.message || 'Something went wrong',
      })
      throw err
    }
  }
  